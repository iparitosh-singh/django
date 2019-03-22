from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    created_on = models.TimeField(auto_now = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg',upload_to = 'post_pics')

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, default =1)
    image = models.ImageField(default ='default_profile.jpg', upload_to ='profile_pics')
    profile_cover = models.ImageField(default='default_cover_pic.jpg', upload_to='cover_pics')
    bio = models.TextField(max_length = 288)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args,**kwargs)

        img = Image.open(self.image.path)
        img1 =Image.open(self.profile_cover.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            image.thumbnail(output_size)
            image.save(self.image.path)

        if img1.height > 200 or img1.width > 200:
            output_size = (300, 300)
            profile_cover.thumbnail(output_size)
            profile_cover.save(self.profile_cover.path)



