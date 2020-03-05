from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .models import Game
from django.views.generic.detail import DetailView
from games.models import Game
from games.forms import GameForm


class GameListView(ListView):
    """ Renders a list of all Games. """
    model = Game

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'home.html', {
          'pages': pages
        })

class GameCreate(TemplateView):
    template_name = 'templates/home.html'
    
    def get(self, request):
        form = GameForm()
        return render(request, self.template_name, {f'form': form})

    def post(self, request):
        form = GameForm(request.POST)
        args = {title: 'title', price: 'price' }
            
        return render(request, self.template_name)
  
class GameDetailsView(DetailView):
    model = Game

    def get(self, request, slug):
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })

def list(request):
    return HttpResponse('Hello, this is list.')

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
