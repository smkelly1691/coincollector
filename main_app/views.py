from django.shortcuts import render
from django.http import HttpResponse

class Coin: 
    def __init__(self, name, year, description, value):
        self.name = name
        self.year = year
        self.description = description
        self.value = value
        
coins = [
    Coin('Morgan Silver Dollar Cull', 1889, 'Vintage Silver dollar', 31.99),
    Coin('Liberty Seated Dollar VG', 1871, 'Liberty seated dollar', 449.99),
    Coin('Draped Bust Dollar VG-8 NGC', 1799, 'Rare Draped Bust Dollar with 13 stars', 1649),
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Welcome to Coin Collector</h1>')

def about(request):
    return render(request, 'about.html')

def coins_index(request):
  return render(request, 'coins/index.html', { 'coins': coins })