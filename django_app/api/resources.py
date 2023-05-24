from rest_framework.viewsets import ModelViewSet

from django_app.api.serializers import TopicCreateSerializer, BlogPostCreateSerializer, \
    CommentCreateSerializer, TopicReadSerializer, BlogPostReadSerializer, CommentReadSerializer
from django_app.models import Topic, Comment, BlogPost


class TopicModelViewSet(ModelViewSet):
    queryset = Topic.objects.all()

    def get_serializer_class(self):
        return TopicReadSerializer if self.request.method == 'GET' else TopicCreateSerializer


class BlogPostModelViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_serializer_class(self):
        return BlogPostReadSerializer if self.request.method == 'GET' else BlogPostCreateSerializer


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)

    def get_serializer_class(self):
        return CommentReadSerializer if self.request.method == 'GET' else CommentCreateSerializer
