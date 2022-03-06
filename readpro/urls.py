
from django.urls import path

from . import views
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('process_image', views.process_image, name='process_image'),
]