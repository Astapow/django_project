from rest_framework import serializers

from django_app.models import BlogPost, Topic, Comment


class TopicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'subscribers']


class BlogPostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['id', 'slug', 'title', 'content', 'created_at', 'updated_at', 'topic', 'author']


class CommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    created_at = serializers.DateField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'content', 'blog_post', 'author']
