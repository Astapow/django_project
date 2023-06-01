from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from django_app.api.serializers import TopicSerializer, BlogPostSerializer, CommentSerializer, \
    UserRegistrationSerializer
from django_app.models import Topic, Comment, BlogPost


class UserRegistrationView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer


class TopicModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def perform_create(self, serializer):
        return serializer.save(subscribers=self.request.user)


class BlogPostModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return BlogPost.objects.filter(author=self.request.user)
        return BlogPost.objects.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
