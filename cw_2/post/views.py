from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# Отображение списка постов
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

# Детальный просмотр поста
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post/post_detail.html', {'post': post})

# Создание нового поста
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post/post_form.html', {'form': form})

# Редактирование поста
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post/post_form.html', {'form': form})

# Удаление поста
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'post/post_confirm_delete.html', {'post': post})