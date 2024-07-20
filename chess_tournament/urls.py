from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Chess Tournament API doc",
        default_version='v1',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email="nilufar20071407@gmail.com"),
        license=openapi.License(name="Chess Tounament blog litsenziyasi"),
    ),
    permission_classes=(permissions.AllowAny,),
    public=True,)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tournament.urls')),
    path('', RedirectView.as_view(url='/api/', permanent=True)),
    path('swagger/',schema_view.with_ui(
        'swagger',cache_timeout=0), name='schema-swagger'),
]
