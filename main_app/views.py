from django.shortcuts import render, redirect
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

def add_appraising(request, coin_id):
  # create a ModelForm instance using the data in request.POST
  form = AppraisingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the coin_id assigned
    new_appraising = form.save(commit=False)
    new_appraising.coin_id = coin_id
    new_appraising.save()
  return redirect('detail', coin_id=coin_id)


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
