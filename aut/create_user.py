from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import banco


class create_user(BaseCommand):
    def create(request, parser, self, *args, **options):
        help = 'Create a new user'
        resultado= banco.sql_query(f"""SELECT COUNT(*) FROM TB_LOGIN""")
        user = []
        for linha in resultado:
            user.append(linha[0])
            username = request.POST.get('username')
            password = request.POST.get('password')

        if username and password:
            parser.add_argument('username', type=str, help='Admin username')
            parser.add_argument('email', type=str, help='Admin email')
            parser.add_argument('password', type=str, help='Admin password')

            username = options.get('nickname')
            mail = options.get('email')
            password = options.get('pass')
                
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username, '', password, mail)
                self.stdout.write(self.style.SUCCESS(f'Usuário "{username}" criado com sucesso.'))
            else:
                self.stdout.write(self.style.WARNING(f'O usuário "{username}" já existe.'))
        
            