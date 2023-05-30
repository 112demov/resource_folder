from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(choices=GENDER, blank=True, max_length=7)
    age = models.IntegerField(blank=True, null=True)
    
    bio = models.TextField()
    city = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return f'{self.user.username}'
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.id)])
