from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, help='Email address of the superuser')
        parser.add_argument('--password', type=str, help='Password of the superuser')
        parser.add_argument('--username', type=str, help='Username of the superuser')

    def handle(self, *args, **options):
        
        User = get_user_model()
        email = options['email']
        password = options['password']
        username = options.get('username', email.split('@')[0])

        if not email or not password:
            self.stdout.write(self.style.ERROR('Email and password are required'))
            return

        try:
            User.objects.create_superuser(email=email, password=password,username=username)
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating superuser: {str(e)}'))