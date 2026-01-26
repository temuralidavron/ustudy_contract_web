from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# from rest_framework import status

from contract.models import Contract


class ContractDeleteAPIView(DestroyAPIView):
    queryset = Contract.objects.all()
    permission_classes = [IsAuthenticated,]

    # permission_classes = [IsAdminUser]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Contract muvaffaqiyatli o‘chirildi"},
            status=200
        )

