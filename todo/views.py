from django.shortcuts import render, redirect

# Create your views here.
from .models import Todo

from .forms import TodoForm

# index home page
def index(request):

    form = TodoForm()
    
    todos = Todo.objects.order_by('id')

    context = {'todos':todos,'form':form}

    return render(request,'todo/index.html',context)

# create new Todos
def add(request):

    form = TodoForm(request.POST)

    if form.is_valid():
        todo  = Todo(text= request.POST['text'])
        todo.save()
    return redirect('home')

# update Todos
def edit(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('home')

def delete(request,todo_id):
    todo = Todo.objects.get(pk=todo_id).delete()
    return redirect('home')

