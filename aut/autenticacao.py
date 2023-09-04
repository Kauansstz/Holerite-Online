from django.contrib.auth.backends import ModelBackend
from django.shortcuts import render
from django.contrib.auth.models import User
from database import banco


class OtherSystemAuthBackend(ModelBackend):
    def authenticate(self, request, registration=None, password=None, **kwargs):
        # authentication logic with the Consinco system
        resultado = banco.sql_query(f"""SELECT COUNT(*) FROM tb_funcionarios WHERE matricula  = '{registration}' and senha = '{password.upper()}'""")
        print(resultado)

        # Storing column values in different variables
        status = []
        for linha in resultado:
            status.append(linha[0])
            

        if registration and password:
            if status[0] == 0:
                # If credentials are correct, create a user in Django
                try:
                    user = User.objects.get(registration=registration)
                except User.DoesNotExist:
                    # Create a new user with the provided password from Consinco
                    
                    user = User.objects.create_user(registration, password=password, is_staff=True, is_superuser=False)
                    user.save()
                return user
            else:
                return render(request, 'menu.html')
        return None


    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None