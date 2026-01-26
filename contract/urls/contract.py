from django.urls import path

from contract.views.create_view import ContractCreateAPIView
from contract.views.destroy_contract import ContractDeleteAPIView
from contract.views.list_contract import ContractListAPIView, ContractDetailAPIView, ContractSavedListAPIView
from contract.views.retrieve_contract import ContractUpdateAPIView

urlpatterns = [
    path('contract/list/', ContractListAPIView.as_view(),name='contract_list'),
    path('contract/saved/list/', ContractSavedListAPIView.as_view(),name='contract_saved_list'),
    path('contract/create/', ContractCreateAPIView.as_view(),name='contract_create'),
    path('contract/detail/<int:pk>/', ContractDetailAPIView.as_view(),name='contract_detail'),
    path('contract/update/<int:pk>/', ContractUpdateAPIView.as_view(),name='contract_update'),
    path('contract/delete/<int:pk>/', ContractDeleteAPIView.as_view(),name='contract_delete'),

]
