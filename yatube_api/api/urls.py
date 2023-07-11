from django.urls import include, path
from rest_framework import routers


from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

VERSION = 'v1/'


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router.register('follow', FollowViewSet, basename='followers')

urlpatterns = [
    path(VERSION, include(router.urls)),
    path(VERSION, include('djoser.urls')),
    path(VERSION, include('djoser.urls.jwt')),
]
