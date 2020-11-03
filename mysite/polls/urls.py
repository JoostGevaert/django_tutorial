from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # does this comma matter?
]

