# dump.py

import os
import django
from django.core.management import call_command

# Cấu hình Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webbanhang.settings')
django.setup()

# Ghi file dumpdata với encoding utf-8 an toàn
with open('data.json', 'w', encoding='utf-8') as f:
    call_command('dumpdata', indent=2, stdout=f)
