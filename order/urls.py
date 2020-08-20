from __future__ import unicode_literals

from rest_framework import routers

from order import views as api_views

router = routers.SimpleRouter()

router.register(r'checkout', api_views.CartCheckOut, basename='cart_checkout')

urlpatterns = []

urlpatterns += router.urls
