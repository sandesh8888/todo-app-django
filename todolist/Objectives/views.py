from django.shortcuts import render
from django.http import HttpResponse
from .models import todo

# Create your views here.
def index(request):
    todo_list = todo.objects.filter(status=0)
    objectives = {
        'objectives': todo_list
    }
    return render(request, 'base.htm', objectives)

def mark_as_done(request, id):
    obj=todo.objects.get(id=id)
    obj.status = True
    obj.save()
    todo_list = todo.objects.filter(status=False)
    objectives = {
        'objectives': todo_list
    }
    return render(request, 'base.htm', objectives)

def new_list(request):
    
    if request.method == "POST":
        dname = request.POST['todo-name']
        obj = todo(name=dname, status=False)
        obj.save()
    print(dname)
    todo_list = todo.objects.filter(status=False)
    objectives = {
        'objectives': todo_list
    }
    return render(request, 'base.htm', objectives)