from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    

class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + "..."
    
        def get_absolute_url(self):
            return reverse('blog-detail', args=[self.id])

    