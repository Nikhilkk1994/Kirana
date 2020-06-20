from rest_framework import routers

from customer import views as api_views

router = routers.SimpleRouter()

router.register(r'user/login', api_views.UserLogin, basename='customer_login')
router.register(r'user/signup', api_views.UserSignUp, basename='customer_signup')

urlpatterns = []

urlpatterns += router.urls
