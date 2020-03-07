from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect 
from .forms import *
from .models import Game
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .models import Game
from .forms import GameForm
from django.urls import reverse_lazy
from django.utils.text import slugify


class GameListView(ListView):
    """ Renders a list of all Games. """
    model = Game

    def get(self, request):
        """ GET a list of games. """
        games = Game.objects.all()
        return render(request, 'list.html', {
          'games': games
        })


class GameCreateView(CreateView):
  """ Renders a Create New Page Form """
  template = 'new_game.html'
  form_class = GameForm
  success_url = '' 

  def get(self, request):
    form = GameForm()
    return render(request, 'new_game.html', {'form': form})

  def post(self, request):
    if request.method == 'POST':
      form = GameForm(request.POST)
      if form.is_valid(): 
        game = form.save()
        return HttpResponseRedirect(reverse_lazy('game-details-page', args = [game.slug]))
      return render(request, 'new_game.html', {'form': form})
    

class GameDetailView(DetailView):
    model = Game


    def get(self, request, slug):
        game = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'one_game.html', {'game': game})


