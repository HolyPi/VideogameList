from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
from . import views


urlpatterns = [
    path('', GameListView.as_view(), name='list'),
    path('<str:slug>/', GameDetailsView.as_view(), name='game-details-page')

]
