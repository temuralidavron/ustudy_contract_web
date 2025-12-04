from django.urls import path

from contract.views.contract import ContractListAPIView, ContractCreateAPIView, ContractDetailAPIView, \
    ContractUpdateAPIView, ContractDeleteAPIView

urlpatterns = [
    path('contract/list/', ContractListAPIView.as_view(),name='contract_list'),
    path('contract/create/', ContractCreateAPIView.as_view(),name='contract_create'),
    path('contract/detail/<int:pk>/', ContractDetailAPIView.as_view(),name='contract_detail'),
    path('contract/update/<int:pk>/', ContractUpdateAPIView.as_view(),name='contract_update'),
    path('contract/delete/<int:pk>/', ContractDeleteAPIView.as_view(),name='contract_delete'),

]