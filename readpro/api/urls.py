from django.urls import path

from . import views

urlpatterns = [
    path('create_user', views.create_user, name='create_user'),
    path('save_word', views.save_word, name='save_word'),
    path('get_word', views.get_word, name='get_word'),
    path('create_object', views.create_object, name='create_object'),
]