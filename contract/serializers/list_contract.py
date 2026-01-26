from rest_framework import serializers

from contract.models import Contract


class ContractListSerializer(serializers.ModelSerializer):
    signature_url = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = '__all__'
        # exclude=('signature',)

    def get_signature_url(self, obj):
        request = self.context.get('request')
        if obj.signature and hasattr(obj.signature, 'url'):
            return request.build_absolute_uri(obj.signature.url)
        return None


class ContractRetrieveSerializer(serializers.ModelSerializer):
    signature_url = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = '__all__'

    def get_signature_url(self, obj):
        request = self.context.get('request')
        if obj.signature and hasattr(obj.signature, 'url'):
            return request.build_absolute_uri(obj.signature.url)
        return None
