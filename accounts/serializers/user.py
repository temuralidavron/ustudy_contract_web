from rest_framework import serializers

from accounts.models import CustomUser
#
#
# class CustomUserCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'email', 'age', 'phone']
#
class CustomUserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'age', 'phone']

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data.get('email'),
            age=validated_data.get('age'),
            phone=validated_data.get('phone'),
        )
        user.set_password(validated_data['password'])  # 🔥 MUHIM
        user.save()
        return user



class CustomUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'age', 'phone']


class CustomUserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'email', 'age', 'phone']