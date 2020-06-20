from __future__ import unicode_literals

from rest_framework import routers

from product import views as api_views

router = routers.SimpleRouter()

router.register(r'category', api_views.CategoryView, basename='category')

urlpatterns = []

urlpatterns += router.urls
