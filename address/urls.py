from __future__ import unicode_literals

from rest_framework import routers

from address import views as api_views

router = routers.SimpleRouter()

router.register(r'user/address', api_views.UserAddressView, basename='user_address')

urlpatterns = []

urlpatterns += router.urls
