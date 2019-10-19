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