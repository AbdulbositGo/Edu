from rest_framework import serializers

from . models import Registry, Payment


class RegistrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Registry
        fields = [
            "id",
            "debit",
            "credit"
        ]
    

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "student",
            "course",
            "registry",
            "amount",
            "date_time",
        ]
        