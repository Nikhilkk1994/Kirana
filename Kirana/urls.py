"""Kirana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from customer import urls as customer_urls
from address import urls as address_urls


schema_view = get_schema_view(
    openapi.Info(
        title='Ration BackEnd Api',
        default_version='v1',
        description='Ration Api'
    ),
    public=True
)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(customer_urls)),
    url(r'^api/', include(address_urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
