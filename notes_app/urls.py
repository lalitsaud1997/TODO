from django.urls import path
from notes_app import views
urlpatterns = [
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete, name='delete')
]
