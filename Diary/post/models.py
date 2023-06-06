from django.db import models
# Create your models here.

#사진업로드 및 글
class Item(models.Model):
    image = models.ImageField(upload_to = 'media', blank=True, null=True)
    location = models.CharField(max_length=200)
    body = models.TextField()
    
    def __str__(self):
        return self.location
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    

    

