from django.urls import path
from notes_app import views
urlpatterns = [
    path('home',views.home)

]
