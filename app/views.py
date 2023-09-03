from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from . import models, serializers

# Create your views here.

class Errors():
    def incorrect_amount_of_get_response():
        return {'ERROR': 'Incorrect amount of get response'}


def get_data(model, serializer, amount, *args):
    match (amount):
        case 'singular':
            if type(*args) == int:
                arg = args[0]
                instance_by_arg = model.objects.get(id=arg)
            else:
                arg = args[0]
                instance_by_arg = model.objects.get(slug=arg)
                
            serialized_intance = serializer(instance_by_arg)
            
            return Response(serialized_intance.data)
        
        case 'popular':
            instances = model.objects.all()
            serialized_intances = serializer(instances, many=True)
            return Response(serialized_intances.data)
        
        case _:
            return Response(Errors.incorrect_amount_of_get_response())
        
        
def query_filter_by_nickname(model, serializer, nickname):
    instance_by_nickname = model.objects.get(nickname=nickname)
    serialized_intance = serializer(instance_by_nickname)
    return Response(serialized_intance.data)
        

@api_view(['GET', 'POST',])
def customers(req):
    if req.method == 'GET':
        customer = req.query_params.get('nickname')
        
        if customer:
            return query_filter_by_nickname(models.Customer, serializers.SerializedCustomer, 'see_only')
        
        else:
            return get_data(models.Customer, serializers.SerializedCustomer, 'popular')
    
    
@api_view(['GET',])
def customer(req, slug):
    if req.method == 'GET':
        return get_data(models.Customer, serializers.SerializedCustomer, 'singular', slug)
    

@api_view(['GET', 'POST',])
def managers(req):
    if req.method == 'GET':
        manager = req.query_params.get('nickname')
        if manager:
            return query_filter_by_nickname(models.Manager, serializers.SerializedManager, '300_u_tractorista')
        
        else:
            return get_data(models.Manager, serializers.SerializedManager, 'popular')
    
    
@api_view(['GET',])
def manager(req, slug):
    if req.method == 'GET':
        return get_data(models.Manager, serializers.SerializedManager, 'singular', slug)
    
    
@api_view(['GET', 'POST',])
def products(req):
    if req.method == 'GET':
        product = req.query_params.get('title')
        
        if product:
            instance_title = models.Product.objects.get(title=product)
            serialized_product = serializers.SerializedProduct(instance_title)
            return Response(serialized_product.data)

        else:
            return get_data(models.Product, serializers.SerializedProduct, 'popular')
    
    
@api_view(['GET',])
def product(req, slug):
    if req.method == 'GET':
        return get_data(models.Product, serializers.SerializedProduct, 'singular', slug)
    

@api_view(['GET', 'POST',])
def delivery_crews(req):
    if req.method == 'GET':
        return get_data(models.DeliveryCrew, serializers.SerializedDeliveryCrew, 'popular')
    
    
@api_view(['GET',])
def delivery_crew(req, slug):
    if req.method == 'GET':
        return get_data(models.DeliveryCrew, serializers.SerializedDeliveryCrew, 'singular', slug)
    
    
@api_view(['GET',])
def cart(req, arg):
    if req.method == 'GET':
        return get_data(models.Cart, serializers.SerializedCart, 'singular', arg)