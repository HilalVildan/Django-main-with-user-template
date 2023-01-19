from django.urls import path, include
from rest_framework import routers
from .views import logout, UserView

router = routers.DefaultRouter()
router.register('users', UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('dj_rest_auth.urls')),

]
