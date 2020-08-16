from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.urls import reverse
from django.dispatch import receiver
import string
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title       = models.CharField(max_length=30)
    body        = RichTextField()
    image       = models.ImageField(upload_to="images")
    url         = models.URLField(max_length=200, null=True)
    hunter      = models.ForeignKey(User, on_delete=models.CASCADE)
    author      = models.CharField(max_length=30)
    date_pub    = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    slug        = models.SlugField(unique=True)
    upvote      = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    


    def get_absolute_url(self):
        return reverse("home", kwargs={"slug": self.pk})


class BlogComment(models.Model):
    sno             = models.AutoField(primary_key=True)
    comment         = models.TextField()
    post            = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp       = models.DateTimeField(auto_now_add=True)
    parent          = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.comment

class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    context = RichTextField()
    def __str__(self):
        return self.context[:20] + " by- " + self.name

@receiver(pre_save,sender=Blog)
def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(pre_save_blog_post_receiver, sender=Blog)
