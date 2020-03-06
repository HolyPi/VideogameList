
from django.urls import path 
from .views import *
from .views import GameListView, GameCreateView, GameDetailView


urlpatterns = [
    path('', GameListView.as_view(), name='list-page'),
    path('new-game/', GameCreateView.as_view(), name='game-create-page'),
    path('<str:slug>/', GameDetailView.as_view(), name='game-details-page'),

]
