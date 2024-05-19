from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Registry, Payment
from .serializers import RegistrySerializers, PaymentSerializers

class RegistryListCreateApiView(ListCreateAPIView):
    serializer_class = RegistrySerializers
    queryset = Registry.objects.all()


class RegistryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RegistrySerializers
    queryset = Registry.objects.all()
    lookup_field = 'pk'


class PaymentListCreateApiView(ListCreateAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()


class PaymentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
    lookup_field = 'pk'



registry_list_create = RegistryListCreateApiView.as_view()
payment_list_create = PaymentListCreateApiView.as_view()

registry_retrive_update_delete = RegistryRetrieveUpdateDestroyAPIView.as_view()
payment_retrive_update_delete = PaymentRetrieveUpdateDestroyAPIView.as_view()