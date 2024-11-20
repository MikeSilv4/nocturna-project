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
        image="https://images.tcdn.com.br/img/img_prod/1156019/penis_de_borracha_realistico_em_silicone_26_5cmx5_3cm_import_377_1_60ac7a89deaf38c19484c1acdd584c05.jpg"
    )