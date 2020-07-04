from __future__ import unicode_literals

from rest_framework import routers

from merchant import views as api_views

router = routers.SimpleRouter()

router.register(r'merchants', api_views.MerchantView, basename='merchants')
router.register(r'merchant', api_views.MerchantProductView, basename='merchant_product')

urlpatterns = []

urlpatterns += router.urls
