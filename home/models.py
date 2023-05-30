from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    body = models.TextField(default = None)
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date']
        
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
        

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(help_text='Input comment')
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-date']
        
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
        
    
