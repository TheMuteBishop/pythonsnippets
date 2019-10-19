from django.db import models
from django.contrib.auth.models import User

from PIL import Image

class Profile(models.Model):
    profile = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics/%Y/%m/%d')

    def __str__(self):
        return self.profile.username

    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)

        img = Image.open(self.profile_pic.path)
        if img.height > 300 or img.width > 300:
            out_size = (300,300)
            img.thumbnail(out_size)
            img.save(self.profile_pic.path)
