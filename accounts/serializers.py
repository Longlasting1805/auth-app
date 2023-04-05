from rest_framework import serializers
from .models import UserData


class UserSerializer(serializers.ModelSerializer):
    is_admin = serializers.BooleanField(default=False)

    class Meta:
        model = UserData
        fields = ["id", "email", "first_name", "last_name", 'password', 'is_admin', 'user_type']

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        if validated_data['is_admin']:
            user.user_type = 'admin'
        else:
            user.user_type = 'student'
        user.save()
        return user

# class AdminSerializer(serializers.ModelSerializer):

#     password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)

#     class Meta:
#         model = UserData
#         fields = ['email', 'name', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         } 

# class StudentSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={"input_type":"password"}, write_only=True)

#     class Meta:
#         model = UserData
#         fields = ['name', 'email', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }

    
class ChangePasswordSerializer(serializers.Serializer):
    model = UserData
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)