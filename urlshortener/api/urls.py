from django.urls import include, path
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="UrlShortener API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="tekin.mertcan@yahoo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,

)
urlpatterns = [

    path('', ApiOverview, name='home'),
    path('short_url', add_url, name='add_url'),
    path('short_url_list', list_url, name='list_url'),
    path('<str:slug>', redirect_url, name='redirect_url'),
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('api/swagger',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]