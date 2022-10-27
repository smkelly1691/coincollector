from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('coins/', views.coins_index, name='index'),
    path('coins/<int:coin_id>/', views.coins_detail, name='detail'),
    path('coins/create/', views.CoinCreate.as_view(), name ='coins_create'),
    path('coins/<int:pk>/update/', views.CoinUpdate.as_view(), name='coins_update'),
    path('coins/<int:pk>/delete/', views.CoinDelete.as_view(), name='coins_delete'),
    path('coins/<int:coin_id>/add_appraising/', views.add_appraising, name='add_appraising'),
    path('shows/', views.ShowList.as_view(), name='shows_index'),
    path('shows/<int:pk>/', views.ShowDetail.as_view(), name='shows_detail'),
    path('shows/create/', views.ShowCreate.as_view(), name='shows_create'),
    path('shows/<int:pk>/update/', views.ShowUpdate.as_view(), name='shows_update'),
    path('shows/<int:pk>/delete/', views.ShowDelete.as_view(), name='shows_delete'),
    path('coins/<int:coin_id>/assoc_show/<int:show_id>/', views.assoc_show, name='assoc_show'),
]
