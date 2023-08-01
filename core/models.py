
from django.db import models

# Create your models here.

class login(models.Model):
    name = models.TextField(max_length= 250)
    email = models.CharField(max_length= 250)
    nickname = models.CharField(max_length= 250)
    password = models.CharField(max_length= 250)

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('O campo "email" é obrigatório')
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using= self.db)
    

#     def creat_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('O superusario precisar ter is_staff=true')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('O superusario precisar ter is_superuser = true')
        
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=100)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

#     objects = CustomUserManager()

#     username_field = 'email'
#     REQUIRED_FIELDS = ['name']

#     def __str__(self):
#         return self.email
    
# class CustomUserCreationForm(forms.ModelForm):
#     password = forms.CharField(label='Senha', widget=forms.PasswordInput)

#     class meta:
#         model = CustomUser
#         fields = ['email', 'name', 'password']

