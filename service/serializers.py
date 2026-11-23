from rest_framework import serializers
from .models import Customer, Device, Technician, ServiceRequest, Invoice, Payment


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            'id',
            'name',
            'phone',
            'email',
            'address',
            'created_at'
        ]


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'id',
            'customer',
            'device_name',
            'brand',
            'model_number',
            'serial_number',
            'problem',
            'created_at'
        ]


class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = [
            'id',
            'name',
            'phone',
            'email',
            'specialization',
            'experience',
            'status',
            'joined_at'
        ]

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = [
            'id',
            'device',
            'technician',
            'problem',
            'priority',
            'status',
            'created_at',
            'updated_at'
        ]


class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'