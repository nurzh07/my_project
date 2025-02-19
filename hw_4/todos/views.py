from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoList, Todo
from .forms import TodoListForm, TodoForm

def todo_list(request):
    return redirect('todo_lists')

def todo_lists(request):
    todo_lists = TodoList.objects.all()
    return render(request, 'todos/todo_lists.html', {'todo_lists': todo_lists})

def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    todos = Todo.objects.filter(todo_list=todo_list)
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_list = todo_list
            todo.save()
            return redirect('todo_list_detail', id=id)
    else:
        form = TodoForm()
    return render(request, 'todos/todo_list_detail.html', {'todo_list': todo_list, 'todos': todos, 'form': form})

def delete_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    todo_list.delete()
    return redirect('todo_lists')

def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    if request.method == 'POST':
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=id)
    else:
        form = TodoListForm(instance=todo_list)
    return render(request, 'todos/edit_todo_list.html', {'form': form})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.delete()
    return redirect('todo_list_detail', id=todo.todo_list.id)

def edit_todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list_detail', id=todo.todo_list.id)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todos/edit_todo.html', {'form': form})
