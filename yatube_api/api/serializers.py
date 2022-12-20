from rest_framework import serializers

from posts.models import Post, User, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.PrimaryKeyRelatedField(read_only=True)
    comments = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group', 'comments')
        read_only_fields = ('author', 'group', 'image')


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'posts')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('author', 'post', 'text', 'created')