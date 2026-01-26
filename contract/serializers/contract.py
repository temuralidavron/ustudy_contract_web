from rest_framework import serializers

from contract.models import Contract


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'id',
            'user',
            'full_name',
            'phone',
            'address',
            'age',
            'document_type',
            'document_series',
            'jshshir',
            'document_given_by',
            'document_given_date',
            'parent_full_name',
            'parent_document_series',
            'parent_jshshir',
            'parent_document_given_by',
            'parent_document_given_date',
            'is_confirmed',
            'saved',
            'created_at',
            'signature'
            'contract_number'


        ]


class ContractDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'id',
            'user',
            'full_name',
            'phone',
            'address',
            'age',
            'document_type',
            'document_series',
            'jshshir',
            'document_given_by',
            'document_given_date',
            'parent_full_name',
            'parent_document_series',
            'parent_jshshir',
            'parent_document_given_by',
            'parent_document_given_date',
            'is_confirmed',
            'saved',
            'created_at',
            'signature'
            'contract_number'


        ]

# class ContractCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contract
#         fields = [
#             'user',
#             'full_name',
#             'phone',
#             'address',
#             'age',
#             'document_type',
#             'document_series',
#             'jshshir',
#             'document_given_by',
#             'document_given_date',
#             'parent_full_name',
#             'parent_document_series',
#             'parent_jshshir',
#             'parent_document_given_by',
#             'parent_document_given_date',
#             'is_confirmed',
#             'saved',
#             'created_at',
#             'signature',
#             'contract_number',
#
#
#         ]
#

class ContractUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'id',
            'user',
            'full_name',
            'phone',
            'address',
            'age',
            'document_type',
            'document_series',
            'jshshir',
            'document_given_by',
            'document_given_date',
            'parent_full_name',
            'parent_document_series',
            'parent_jshshir',
            'parent_document_given_by',
            'parent_document_given_date',
            'is_confirmed',
            'saved',
            'created_at',
            'signature'
            'contract_number'


        ]