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

  
class GameDetailView(DetailView):
    model = Game

    def get(self, request, slug):
        game = Game.objects.get(slug=slug)
        return render(request, 'one_game.html', {
          'game': game
        })


class GameCreateView(CreateView):
    template_name = 'new_game.html'
    form_class = GameForm
    success_url = reverse_lazy('list-page')

    def form_valid(self, *args, **kwargs):
      
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

  
        return super(Game, self).save(*args, **kwargs)

      



# def Image_upload(request): 
  
#     if request.method == 'POST': 
#         form = GameForm(request.POST, request.FILES) 
  
#         if form.is_valid(): 
#             form.save() 
#             print(form.title)
#             return redirect('success')
#     else: 
#         form = GameForm() 
#     return render(request, 'game_img_form.html', {'form' : form}) 
    
  
  
# def success(request): 
#     return HttpResponse('successfully uploaded')
