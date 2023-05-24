from django.urls import path, include
from rest_framework import routers
from .resources import TopicModelViewSet, BlogPostModelViewSet, CommentModelViewSet


router = routers.SimpleRouter()
router.register('topic', TopicModelViewSet)
router.register('blog_post', BlogPostModelViewSet)
router.register('comment', CommentModelViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
