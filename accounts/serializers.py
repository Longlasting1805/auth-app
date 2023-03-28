from rest_framework import serializers
from .models import UserData, Admin, Student


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserData
        fields = ["id", "email", "name"]

    def create(self, validated_data):
        user = UserData.objects.create(email=validated_data['email'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user

class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin     
        fields = ["user"]   

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student     
        fields = ["user"]   

class ChangePasswordSerializer(serializers.Serializer):
    model = UserData
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)