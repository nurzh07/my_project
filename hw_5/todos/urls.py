from django.urls import path
from . import views
from .views import edit_todo
from .views import delete_todo
from .views import register
from .views import todo_detail

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('todos/', views.todo_list, name='todo_list'),
    path('todos/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todos/new/', views.create_todo, name='create_todo'),
    path('todos/<int:id>/delete/', views.delete_todo, name='delete_todo'),
    path('<int:id>/edit/', edit_todo, name='edit_todo'),
    path('<int:id>/delete/', delete_todo, name='delete_todo'),
    path('register/', register, name='register'),
    path('<int:id>/', todo_detail, name='todo_detail'),

]
