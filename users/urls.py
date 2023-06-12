from django.urls import path, include
from .views import RegisterView
from rest_framework import routers

router = routers.DefaultRouter()
router.register("register", RegisterView)

urlpatterns = [
  path("", include(router.urls)),
  path('auth/', include('dj_rest_auth.urls'))
]