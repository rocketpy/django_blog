from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#  for update use:  python manage.py makemigrations blog_app
# second command:  python manage.py migrate blog_app


class Language(models.Model):
    name = models.CharFireld(max_length=50)
    paradigm = models.CharField(max_length=50)


"""
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
"""
"""
class NewMember(models.Model):
    first_name= models.CharField(max_length=200)
    last_name= models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    website= models.URLField(max_length=250)
"""
