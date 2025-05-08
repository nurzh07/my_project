from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Todo
from .forms import TodoForm
from django.contrib.auth.forms import UserCreationForm

@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id)

    # Проверяем, является ли текущий пользователь владельцем задачи
    if todo.user != request.user:
        return render(request, 'todos/forbidden.html', status=403)

    return render(request, 'todos/todo_detail.html', {'todo': todo})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})

# Страница логина
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('todo_list')
    return render(request, 'login.html')

# Выход пользователя
def logout_view(request):
    logout(request)
    return redirect('login')

# Список todos только для залогиненного пользователя
@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todos/list.html', {'todos': todos})

# Детальный просмотр todo
@login_required
def todo_detail(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    return render(request, 'todos/detail.html', {'todo': todo})

# Создание todo (используем Django Forms)
@login_required
def create_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todos/create.html', {'form': form})

# Удаление todo (только если это его todo)
@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.user == todo.user:
        todo.delete()
        return redirect('todo_list')
    else:
        return HttpResponseForbidden("Вы не можете удалить этот todo.")

@login_required
def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todos/edit_todo.html', {'form': form})

@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('todo_list')
