#from django.conf import settings
from django.db import models

# Create your models here.
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
class Post(models.Model):
    title = models.CharField(max_length=200)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    #author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField
    published_date = models.DateTimeField

    def __str__(self):
        return self.title + " " + '|'+ " " + str(self.author)