from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets, permissions
from djoser.views import UserViewSet


from posts.models import Post, Group, Comment, User, Follow
from .serializers import PostSerializer, GroupSerializer
from .serializers import CommentSerializer
from .serializers import CustomUserSerializer
from .serializers import FollowSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import LimitOffsetPagination


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = LimitOffsetPagination 

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        return post.comments.all()

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all
    serializer_class = FollowSerializer
    permission_classes = [ IsOwnerOrReadOnly,]

    def get_queryset(self):
        user=self.request.user
        return Post.objects.filter(author__following__user=user)


