from django.urls import path
from . import views
from django.urls import path
urlpatterns = [
    path('', views.index),
    path('myvis', views.myvis),
    path('favou', views.favou),
    path('myimp', views.myimp),
    path('mylin', views.mylin),
]
