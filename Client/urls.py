from django.urls import include, path

from rest_framework import routers

from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls')),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
router = DefaultRouter()
router.register(r"user",UserViewSet, basename="user")
urlpatterns += router.urls