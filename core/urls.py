from django.contrib import admin
from django.urls import path
from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="My API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # apis
    path("api/user/", include("src.apps.user.api.urls")),
    path("api/item/", include("src.apps.items.api.urls")),
    path("api/sales/", include("src.apps.sales.api.urls")),
    # dash
    path("dash/home/", include("src.apps.home.dash.urls")),
    path("dash/sales/", include("src.apps.sales.dash.urls")),
    path("dash/user/", include("src.apps.user.dash.urls")),
]
