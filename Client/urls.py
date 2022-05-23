from django.urls import include, path

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import *
router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)

urlpatterns = [
   path('api/', include(router.urls)),
   path('api-auth/', include('rest_framework.urls')),
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('', PersonList.as_view(),name='persons'),
   path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),

]
router = DefaultRouter()
router.register(r"user",UserViewSet, basename="user")
router.register(r"person",PersonViewSet, basename="person")
urlpatterns += router.urls
