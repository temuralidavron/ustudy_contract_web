from rest_framework.generics import CreateAPIView
from rest_framework.permissions import  IsAuthenticated

from contract.models import Contract
from contract.serializers.create_contract import ContractCreateSerializer


class ContractCreateAPIView(CreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractCreateSerializer
    permission_classes = [IsAuthenticated,]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



