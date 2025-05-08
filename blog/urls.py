from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from rest_framework_nested.routers import NestedSimpleRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

posts_router = NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]
