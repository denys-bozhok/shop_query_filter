from rest_framework import serializers

from .models import *


class SerializedManager(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'


class SerializedProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SerializedCart(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class SerializedDeliveryCrew(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCrew
        fields = '__all__'


class SerializedCustomer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

