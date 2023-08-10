import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","thirds.settings")
import django
django.setup()
from third_app.models import mod
def insert(names,emails,passwords):
    mod.objects.get_or_create(username=names,email=emails,password=passwords)