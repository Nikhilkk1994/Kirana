from __future__ import unicode_literals

from rest_framework import routers

from product import views as api_views

router = routers.SimpleRouter()

router.register(r'category', api_views.CategoryView, basename='category')
router.register(r'product/keyword', api_views.ProductKeywordSearch, basename='product_search')

urlpatterns = []

urlpatterns += router.urls
