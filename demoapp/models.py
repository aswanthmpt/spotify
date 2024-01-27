from django.db import models

# Create your models here.
class Data(models.Model):
    name=models.CharField(max_length=250)
    text=models.TextField()
    image=models.ImageField(upload_to='place')
    
    def __str__(self):
        return self.name