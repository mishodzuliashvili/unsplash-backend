from django.contrib import admin
from django.urls import include, path
from photo_item.views import PhotoItemViewSet
from rest_framework.routers import DefaultRouter
from .views import CustomAuthToken
from django.urls import re_path 
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="My Unsplash API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



router = DefaultRouter()

router.register('photos',PhotoItemViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('',include(router.urls)),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api/token/', CustomAuthToken.as_view()),
   re_path('login',views.login),
   re_path('signup',views.signup),
   re_path('test_token',views.test_token),
   path('check_password',views.check_password),
]
  