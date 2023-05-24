from rest_framework import serializers

from django_app.models import BlogPost, Topic, Comment


class TopicReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'description', 'subscribers']


class TopicCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['title', 'description']


class BlogPostReadSerializer(serializers.ModelSerializer):
    topic = TopicReadSerializer(many=True)
    author = serializers.StringRelatedField()

    class Meta:
        model = BlogPost
        fields = ['id', 'slug', 'title', 'content', 'created_at', 'updated_at', 'topic', 'author']


class BlogPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

    def create(self, validated_data):
        return BlogPost.objects.create(**validated_data)


class CommentReadSerializer(serializers.ModelSerializer):
    blog_post = BlogPostReadSerializer()
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['id', 'created_at', 'content', 'blog_post', 'author']


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)
