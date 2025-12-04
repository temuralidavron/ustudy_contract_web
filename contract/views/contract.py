from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from contract.models import Contract
from contract.serializers.contract import ContractListSerializer, ContractDetailSerializer, ContractCreateSerializer, \
    ContractUpdateSerializer


class ContractListAPIView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer


class ContractDetailAPIView(RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer

class ContractCreateAPIView(CreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractCreateSerializer

class ContractUpdateAPIView(UpdateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractUpdateSerializer

class ContractDeleteAPIView(DestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer
