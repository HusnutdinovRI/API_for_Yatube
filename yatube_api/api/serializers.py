import base64

from rest_framework import serializers

from djoser.serializers import UserSerializer

from django.core.files.base import ContentFile

from posts.models import Group, Post, Comment, User, Follow


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


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
    image = Base64ImageField(required=False, allow_null=True)

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

    user = serializers.SlugRelatedField(read_only=True, slug_field="username")
    following = serializers.SlugRelatedField(queryset=User.objects.all(),
                                             slug_field="username")

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate(self, validated_data):
        user = self.context['request'].user
        following = Follow.objects.filter(
            user=user, following=validated_data['following'])
        if user == validated_data['following']:
            raise serializers.ValidationError(
                'Ошибка! Нельзя подписаться на себя')
        if len(following) > 0:
            raise serializers.ValidationError(
                'Ошибка! Нельзя подписаться на автора два раза')
        return validated_data
