
from django.urls import path 
from .views import *
from .views import GameDetailView, GameListView, GameCreateView


urlpatterns = [
    path('', GameListView.as_view(), name='list-page'),
    path('new-game/', GameCreateView.as_view(), name='game-create-page'),
    path('<slug>/', GameDetailView.as_view(), name='game-details-page'),

]
