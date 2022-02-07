from django.shortcuts import redirect, render
import notes_app
from notes_app.models import Notes

# Create your views here.
def home(request):
    notes=Notes.objects.all()
    return render(request,'notes_app/home.html',{'note':notes})

def add(request):
    if request.method == 'GET':
        return render(request,'notes_app/add.html')
    else:
        title = request.POST['title']
        description = request.POST['description']
        Notes.objects.create(title=title,description=description,is_completed=False)

        return redirect('home')

def edit(request):
    if request.method == 'GET':
        return render(request, 'notes_app/edit.html')


