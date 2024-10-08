from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from user.models.client_model import ClientModel
from user.serializers.client_serializer import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['user__first_name', 'user__last_name']