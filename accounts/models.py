from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token
from django.conf import settings

# Create your models here.

@receiver(reset_password_token_created)
def reset_password_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = '{}?token={}'.format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        'password reset for {title}'.format(title='some website title'),
        # message:
        email_plaintext_message,
        # from:
        'noreply@somehost.local',
        # to:
        [reset_password_token.user.email]

    )

class UserManager(BaseUserManager):

    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)    
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)

class UserData(AbstractUser):
    USER_TYPE = (
        ('ADMIN', 'admin'),
        ('STUDENT', 'student'),
    )
       

    username = None
    user_type = models.CharField(max_length=50, choices=USER_TYPE, default='admin')
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 

    objects = UserManager()
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.first_name  

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.users = self.base_role
    #         return super().save(*args, **kwargs) 

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)          

# class Admin(models.Model):
#     user = models.OneToOneField(UserData, on_delete=models.CASCADE,primary_key=True)
#     admin_name = models.CharField(max_length=100, null=True)

#     def __str__(self):
#        return str(self.user)

# class Student(models.Model):
#     user = models.OneToOneField(UserData, on_delete=models.CASCADE,primary_key=True)  
#     student_name = models.CharField(max_length=100,null=True)  

    def __str__(self):
       return str(self.user)
        