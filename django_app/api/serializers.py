from django.contrib.auth.models import User
from rest_framework import serializers

from django_app.models import BlogPost, Topic, Comment


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class TopicSerializer(serializers.ModelSerializer):
    subscribers = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'subscribers']


class BlogPostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'slug', 'title', 'content', 'created_at', 'updated_at', 'topic', 'author']


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'content', 'blog_post', 'author']
