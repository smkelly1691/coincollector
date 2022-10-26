from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coin
from .forms import AppraisingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def coins_index(request):
    coins = Coin.objects.all()
    return render(request, 'coins/index.html', { 'coins': coins })

def coins_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    appraising_form = AppraisingForm()
    return render(request, 'coins/detail.html', { 'coin': coin, 'appraising_form': appraising_form})

class CoinCreate(CreateView):
  model = Coin
  fields = '__all__'
#   success_url = '/coins/'

class CoinUpdate(UpdateView):
    model = Coin
    fields = ['year', 'description', 'value']
    
class CoinDelete(DeleteView):
    model = Coin
    success_url = '/coins/'
