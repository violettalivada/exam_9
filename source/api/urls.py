from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ImageViewSet

app_name = 'api'

router = DefaultRouter()
router.register('image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
