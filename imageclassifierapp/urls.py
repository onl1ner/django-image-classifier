from django.urls import path

from . import views

app_name = 'imageclassifierapp'

urlpatterns = [
    path('', views.main, name='main')
]