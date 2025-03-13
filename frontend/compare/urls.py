from django.urls import path
from .views import compare_images

urlpatterns = [
    path('compare/', compare_images, name='compare_images'),
]