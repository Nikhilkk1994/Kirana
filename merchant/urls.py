from __future__ import unicode_literals

from rest_framework import routers

from merchant import views as api_views

router = routers.SimpleRouter()

router.register(r'merchant', api_views.MerchantView, basename='merchants')

urlpatterns = []

urlpatterns += router.urls
