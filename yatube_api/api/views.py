from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .serializers import PostSerializer, UserSerializer, GroupSerializer, CommentSerializer
from posts.models import Post, User, Group, Comment


class PostViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, id=pk)
        serializer = PostSerializer(post)

        return Response(serializer.data)

    def update(self, request, pk=None):
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(post, data=request.data)

        if request.user != post.author:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        post = get_object_or_404(Post, id=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)

        if request.user != post.author:

            return Response(status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, id=pk)

        if request.user != post.author:

            return Response(status=status.HTTP_403_FORBIDDEN)

        post.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_queryset = Comment.objects.filter(post=post_id)

        return new_queryset
