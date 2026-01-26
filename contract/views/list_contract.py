from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from contract.models import Contract
from contract.serializers.list_contract import ContractListSerializer, ContractRetrieveSerializer


class ContractListAPIView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer
    permission_classes = [IsAuthenticated,]


    def get_queryset(self):
        return Contract.objects.filter(saved=False)





class ContractDetailAPIView(RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractRetrieveSerializer
    permission_classes = [IsAuthenticated,]





class ContractSavedListAPIView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer
    permission_classes = [IsAuthenticated,]