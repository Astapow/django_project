from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext as _

TOPIC_CHOICES = (
    (1, _("Not selected")),
    (2, _("Sport")),
    (3, _("Fishing")),
    (4, _("Tourism")),
    (5, _("Other"))
)


class Topic(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True)
    subscribers = models.ManyToManyField(User)

    def __str__(self):
        return self.title


class BlogPost(models.Model):
    slug = models.SlugField(verbose_name='URL', max_length=50, unique=True)
    title = models.TextField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    topic = models.ManyToManyField(Topic)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.IntegerField(choices=TOPIC_CHOICES, default=1)

    def __str__(self):
        return f"\
        title: {self.title} content: {self.content} author: {self.author.username} categories: {self.categories}"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)


class Comment(models.Model):
    created_at = models.DateField(auto_now=True)
    content = models.TextField(max_length=100)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, related_name='get_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content} {self.author.username} {self.blog_post}"



# ORM
# user1 = User.objects.first()
# user2 = User.objects.all()[1]
# user3 = User.objects.last()
# topic1 = Topic.objects.create(title='test1 title', description='test1 description')
# topic2 = Topic.objects.create(title='test2 title', description='test2 description')
# topic1.subscribers.add(user1)
# topic2.subscribers.add(user2)
# post1 = BlogPost.objects.create(author=user1, slug='test1', title='title test1', content='some content', categories='2')
# post2 = BlogPost.objects.create(author=user2, slug='test2', title='title test2', content='second content',
#                                 categories='2')
# post3 = BlogPost.objects.create(author=user3, slug='TESTED', title='last test', content='last content', categories='3')
# post1.topic.add(topic1)
# post2.topic.add(topic2)
# post3.topic.add(topic2)
# post4 = BlogPost.objects.create(author=user2, slug='some-1', title='SOME test', content='SOME content', categories='2')
# post5 = BlogPost.objects.create(author=user1, slug='some-2', title='SOME test2', content='SOME content2',
#                                 categories='3')
# post6 = BlogPost.objects.create(author=user2, slug='some-3', title='SOME test3', content='SOME content3',
#                                 categories='3')
# post4.topic.add(topic2)
# post5.topic.add(topic1)
# post6.topic.add(topic1, topic2)
# comment1 = Comment.objects.create(author=user1, blog_post=post5, content='my commit 1')
# comment2 = Comment.objects.create(author=user1, blog_post=post1, content='my commit 2')
# comment3 = Comment.objects.create(author=user2, blog_post=post2, content='my commit 3')
# comment4 = Comment.objects.create(author=user2, blog_post=post4, content='my commit 4')
# comment5 = Comment.objects.create(author=user2, blog_post=post6, content='my commit 5')
# comment6 = Comment.objects.create(author=user3, blog_post=post6, content='my commit 6')
