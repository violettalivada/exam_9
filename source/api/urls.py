from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ImageViewSet, CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register('image', ImageViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
