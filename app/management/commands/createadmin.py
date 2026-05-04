from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin user if not exists'

    def handle(self, *args, **kwargs):
        username = "Admin"
        email = "admin@gmail.com"
        password = "21071999"

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username, email, password)
            self.stdout.write(self.style.SUCCESS("Admin created"))
        else:
            self.stdout.write("Admin already exists")