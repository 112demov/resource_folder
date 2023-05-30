from django.db import models
import PIL
from django.urls import reverse


class Picture(models.Model):

    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=120)
    alt = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    
    
    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('foto', args=[str(self.id)])
