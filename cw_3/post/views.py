from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Thread, Post
from .forms import ThreadForm, PostForm

# Главная страница, перенаправление на список Threads
def home(request):
    return redirect('threads_list')

# Список всех Thread
def threads_list(request):
    threads = Thread.objects.all()
    return render(request, 'post/threads_list.html', {'threads': threads})

# Создание нового Thread
def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('threads_list')
    else:
        form = ThreadForm()
    return render(request, 'post/create_thread.html', {'form': form})

# Детали Thread
def thread_detail(request, id):
    thread = get_object_or_404(Thread, id=id)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'post/thread_detail.html', {'thread': thread, 'posts': posts})

# Создание нового Post для Thread
def create_post(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            return redirect('thread_detail', id=thread.id)
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form, 'thread': thread})

# Удаление Thread
def delete_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    thread.delete()
    return redirect('threads_list')

# Редактирование Thread
def edit_thread(request, id):
    thread = get_object_or_404(Thread, id=id)
    if request.method == 'POST':
        form = ThreadForm(request.POST, instance=thread)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=thread.id)
    else:
        form = ThreadForm(instance=thread)
    return render(request, 'post/edit_thread.html', {'form': form})

# Удаление Post
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    thread_id = post.thread.id
    post.delete()
    return redirect('thread_detail', id=thread_id)

# Редактирование Post
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('thread_detail', id=post.thread.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post/edit_post.html', {'form': form})
