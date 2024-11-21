import django
import os
import requests
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()                                                                                                                                              
from time import sleep

from src.apps.items.models import Items   
from src.apps.items.api.serializers import ItemsAllFieldsSerializer         

for i in range(1000):
    Items.objects.create(
        name=f"Vibrador {i}k",
        brand="test",
        model="test",
        description="test",
        category="vibradores",
        stock_quantity=10,
        value=1,
        image="https://instagram.fppb10-1.fna.fbcdn.net/v/t51.2885-15/81122307_838055663297248_3746289774751538260_n.jpg?stp=dst-jpg_e35&efg=eyJ2ZW5jb2RlX3RhZyI6ImltYWdlX3VybGdlbi4xMDgweDEwODAuc2RyLmYyODg1LmRlZmF1bHRfaW1hZ2UifQ&_nc_ht=instagram.fppb10-1.fna.fbcdn.net&_nc_cat=104&_nc_ohc=IP-0G8SRczUQ7kNvgGuP6KH&_nc_gid=2446816ba87646aeba5cbc136246cc0c&edm=ALQROFkBAAAA&ccb=7-5&ig_cache_key=MjIwNjk5Njc1ODA2NjY3NDY3OQ%3D%3D.3-ccb7-5&oh=00_AYD-O--nFbj1z4sc888-BMbm4dx_2Co9ZyDWzTFckh_bsA&oe=674409DE&_nc_sid=fc8dfb"
    )