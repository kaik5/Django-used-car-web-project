from django.db import models

# Create your models here.
class Team(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    title = models.CharField(max_length = 255)
    photo = models.ImageField(upload_to = 'photos/%d/%m/%Y')
    facebook_link = models.URLField(max_length = 100)  
    twitter_link = models.URLField(max_length = 100)
    google_plus_link = models.URLField(max_length = 100)
    created_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.first_name + " " + self.last_name;