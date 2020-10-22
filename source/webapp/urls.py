from django.urls import path, include

from webapp.views import *

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='image_view'),
    path('image/add/', ImageCreateView.as_view(), name='image_create'),
    path('image/<int:pk>/update/', ImageUpdateView.as_view(), name='image_update'),
    path('image/<int:pk>/delete/', ImageDeleteView.as_view(), name='image_delete'),
]