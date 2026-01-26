from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView

from contract.models import Contract
from contract.serializers.contract import ContractListSerializer, ContractDetailSerializer


class ContractListAPIView(ListAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer

    def get_queryset(self):
        return Contract.objects.filter(saved=False)


class ContractDetailAPIView(RetrieveAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractDetailSerializer





#
# class ContractUpdateAPIView(UpdateAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractUpdateSerializer
#
#     def perform_update(self, serializer):
#         serializer.save(saved=True, is_confirmed=True)

class ContractDeleteAPIView(DestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractListSerializer





## contract/pdf.py
# from django.template.loader import render_to_string
# from weasyprint import HTML
# from django.http import HttpResponse
#
# def contract_pdf_view(request, pk):
#     contract = Contract.objects.get(pk=pk, user=request.user, saved=True)
#
#     html_string = render_to_string(
#         'contract_pdf.html',
#         {'contract': contract}
#     )
#
#     html = HTML(string=html_string)
#     pdf = html.write_pdf()
#
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'filename="contract.pdf"'
#     return response
