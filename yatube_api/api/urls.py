from rest_framework import routers
from django.urls import include, path


from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = routers.DefaultRouter()
router.register('api/v1/posts', PostViewSet, basename='posts')
router.register('api/v1/groups', GroupViewSet, basename='groups')
router.register(r'api/v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register('api/v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router.urls)),
]
