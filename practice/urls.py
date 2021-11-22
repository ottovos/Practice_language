from django.urls import path
from . import views

urlpatterns = [
    path('', views.practiceWords, name='practice'),
    path('addWords', views.addWords, name='add words'),
]