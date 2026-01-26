import re

from rest_framework import serializers

from contract.models import Contract


class ContractCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        exclude = (
            'saved',
            'contract_number',
            'initial_price',
            'user',
        )

    def validate_document_given_by(self, value):


        # Faqat harf, bo‘sh joy va zarur belgilar (.,-№)
        pattern = r'^[A-Za-zА-Яа-яЁё0-9\s\.,\-№]+$'
        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError(
                "Document given by faqat harflar, raqamlar va nuqta, vergul, tire, № belgilarini o‘z ichiga olishi mumkin"
            )
        return value.strip()

    def validate_jshshir(self, value):
        # 14 ta raqam bo'lishi kerak
        pattern = r'^\d{14}$'
        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError(
                "JSHSHIR faqat 14 raqamdan iborat bo‘lishi kerak"
            )
        return value

    def validate_parent_jshshir(self, value):
        # 14 ta raqam bo'lishi kerak
        pattern = r'^\d{14}$'
        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError(
                "JSHSHIR faqat 14 raqamdan iborat bo‘lishi kerak"
            )
        return value

    def validate_document_series(self, value):
        # Regex: 2 harf (A-Z) + optional space + 7 raqam
        pattern = r'^[A-Z]{2}\s?\d{7}$'
        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError(
                "Document series faqat AA1234567 yoki AA 1234567 formatida bo‘lishi kerak"
            )
        return value

    def validate_parent_document_series(self, value):
        # Regex: 2 harf (A-Z) + optional space + 7 raqam
        pattern = r'^[A-Z]{2}\s?\d{7}$'
        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError(
                "Document series faqat AA1234567 yoki AA 1234567 formatida bo‘lishi kerak"
            )
        return value

    def validate_phone(self, value):
        # Regex: +998 bilan boshlanadi va faqat raqam, jami uzunligi 13
        pattern = r'^\+998\d{9}$'
        if not re.fullmatch(pattern, value):
            raise serializers.ValidationError(
                "Phone raqami +998 bilan boshlanishi va jami 13 ta belgidan oshmasligi kerak"
            )
        return value

    def validate_name_field(self, value, field_name):
        if not re.fullmatch(r'[A-Za-z]+', value):
            raise serializers.ValidationError(
                f"{field_name} faqat lotin harflaridan iborat bo‘lishi kerak"
            )
        return value


    def validate_first_name(self, value):
        return self.validate_name_field(value, "First name")

    def validate_last_name(self, value):
        return self.validate_name_field(value, "Last name")

    def validate_middle_name(self, value):
        return self.validate_name_field(value, "Middle name")

    def validate(self, attrs):
        age = attrs.get('age')

        if age is None:
            raise serializers.ValidationError({"age": "Yosh kiritilishi shart"})

        # 🔴 Agar 18 dan kichik bo‘lsa
        if age < 18:
            required_parent_fields = [
                'parent_full_name',
                'parent_document_series',
                'parent_jshshir',
                'parent_document_given_by',
                'parent_document_given_date',
            ]

            errors = {}
            for field in required_parent_fields:
                if not attrs.get(field):
                    errors[field] = "Bu maydon 18 yoshdan kichiklar uchun majburiy"

            if errors:
                raise serializers.ValidationError(errors)

        return attrs

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
