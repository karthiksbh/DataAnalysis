from .views import *
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='homepage'),
    path('data/', views.index, name='table'),
    path('turkish/', views.turkish, name='tableturk'),
    path('caucasian/', views.caucasian, name='tablecau'),
    path('korean/', views.korean, name='tablekor'),
    path('brazil/', views.brazil, name='tablebraz'),
    path('indian/', views.indian, name='tableind'),
    path('german/', views.german, name='tableger'),
    path('srilankan/', views.srilankan, name='tablesril'),
    path('taiwanese/', views.taiwanese, name='tabletaiw'),
    path('male/', views.male, name='tablemale'),
    path('female/', views.female, name='tablefemale'),
    path('searchof/', views.search, name='search'),
    path('search/', views.searchop, name='searchop')
]
