from rest_framework.viewsets import ModelViewSet

from django_app.api.serializers import TopicSerializer, BlogPostSerializer, CommentSerializer
from django_app.models import Topic, Comment, BlogPost


class TopicModelViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class BlogPostModelViewSet(ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
