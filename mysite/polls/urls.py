from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/results
    path('<int:question_id/', views.detail, name='detail'), # does this comma matter?
]

