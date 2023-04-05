from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, ChangePasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django_email_verification import send_email
from django.views.decorators.csrf import csrf_exempt
from django_email_verification import verify_view, verify_token
from rest_framework import generics
from .models import UserData
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ChangPasswordView(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = UserData
    permission_classes = (IsAuthenticated, )

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get('old_password')):
                return Response({'old password': ['wrong password. ']}, status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get('new_password'))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'password updated successfully',
                'data': []
            }            

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        



@verify_view  
def confirm(request, token):
    success, user = verify_token(token)
    return httpResponse((f'Account verified, {user.username}' if success else 'Invalid token'))     

def sendEmail(request):
    send_mail(
    'Please verify your email',
    'This is an automated message from django',
    'kenkenny1805@gmail.com',
    ['longlasting1805@gmail.com'],
    fail_silently=False
    )
    return render(request, 'confirm.html')           
