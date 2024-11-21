from django.urls import path
from django.urls import include

app_name = 'src.apps.home.dash'

# views
from src.apps.home.dash.views import (
    catalog,
    homepage,
    contacts,
    sucess,
)

urlpatterns = [
    path("catalog/", catalog, name="catalog-dash"),
    path("", homepage, name="homepage-dash"),
    path("contacts/", contacts, name="contacts-dash"),
    path("sucess/", sucess, name="sucess-dash"),
]