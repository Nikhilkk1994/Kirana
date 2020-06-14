from __future__ import unicode_literals

from rest_framework import routers

from customer import views as api_views

router = routers.SimpleRouter()

router.register(r'customer/login', api_views.UserLogin, basename='customer_login')

urlpatterns = []

urlpatterns += router.urls
