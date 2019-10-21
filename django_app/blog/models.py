from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class PostManager(models.Manager):
    def top_posts(self):
        return self.get_queryset().order_by('-date_posted')[:5]

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog-detail', kwargs={'pk': self.pk})

class CommentManager(models.Manager):
    def approved_comments(self):
        return self.get_queryset().filter(is_public=True)

    def not_approved_comments(self):
        return self.get_queryset().filter(is_public=False)

    def commented_by(self, user):
        return self.get_queryset().filter(op=user)
    
    def for_post(self, post):
        return self.get_queryset().filter(is_public=True).filter(post=post).filter(parent=None)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    op = models.ForeignKey(User, on_delete=models.CASCADE,related_name='poster')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    objects = CommentManager()
    def approve(self):
        self.is_public = True
        self.save()

    def __str__(self):
        return f"{' '.join(self.body.split()[:20])}...."