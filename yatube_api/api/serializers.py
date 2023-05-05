from rest_framework import serializers

from djoser.serializers import UserSerializer

from posts.models import Group, Post, Comment, User, Follow


class CustomUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        fields = ('__all__')
        model = Post
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('__all__')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        model = Follow
