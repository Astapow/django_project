from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from django_app.api.permissions import IsAdminOrReadOnlyPermission
from django_app.api.serializers import TopicSerializer, BlogPostSerializer, CommentSerializer, \
    UserRegistrationSerializer
from django_app.models import Topic, Comment, BlogPost


class UserRegistrationView(ModelViewSet):
    permission_classes = [IsAdminOrReadOnlyPermission]
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return User.objects.all()
            else:
                return User.objects.filter(username=self.request.user)
        else:
            return None


class TopicModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Topic.objects.all()
            else:
                return Topic.objects.filter(subscribers=self.request.user)
        else:
            return Topic.objects.all()


class BlogPostModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return BlogPost.objects.all()
            else:
                return BlogPost.objects.filter(author=self.request.user)
        else:
            return BlogPost.objects.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentModelViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return Comment.objects.all()
            else:
                return Comment.objects.filter(author=self.request.user)
        else:
            return Comment.objects.all()

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)
