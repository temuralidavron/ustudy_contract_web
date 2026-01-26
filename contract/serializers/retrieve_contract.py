from rest_framework import serializers
from rest_framework.generics import CreateAPIView

from contract.models import Contract


class ContractAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'user',
            'first_name',
            'last_name',
            'middle_name',
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
            'signature',
            'contract_number',
            'initial_price',

        ]
    def validate(self, attrs):
        instance = self.instance
        age = attrs.get('age', instance.age if instance else None)

        if age < 18 and not attrs.get('parent_full_name', instance.parent_full_name):
            raise serializers.ValidationError(
                {"parent_full_name": "Majburiy"}
            )
        return attrs







