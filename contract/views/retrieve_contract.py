from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from contract.models import Contract
from contract.serializers.retrieve_contract import ContractAdminSerializer


class ContractUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractAdminSerializer
    permission_classes = [IsAuthenticated]