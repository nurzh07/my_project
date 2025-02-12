from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post
from .forms import PostForm

# API: Получить список постов
def get_posts(request):
    posts = Post.objects.all().values('id', 'title', 'description', 'author')
    return JsonResponse(list(posts), safe=False)

# API: Получить один пост
def get_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return JsonResponse({'id': post.id, 'title': post.title, 'description': post.description, 'author': post.author})

# API: Создать новый пост
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return JsonResponse({'id': post.id, 'title': post.title, 'description': post.description, 'author': post.author})
    else:
        form = PostForm()
    return render(request, 'post/create_post.html', {'form': form})

# API: Удалить пост
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('/posts/')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

