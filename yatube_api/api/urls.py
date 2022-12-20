from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from django.urls import path, include

from .views import PostViewSet, UserViewSet, GroupViewSet, CommentViewSet


router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register('posts/<int:pk>/comments/', CommentViewSet, basename='comments')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
]
