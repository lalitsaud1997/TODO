from audioop import add
from unicodedata import name
from django.urls import path
from notes_app import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('edit/',views.edit,name='edit'),
]
