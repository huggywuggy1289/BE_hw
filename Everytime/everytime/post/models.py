from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    is_anonymous = models.BooleanField(default="True")
    

    def __str__(self):
        return self.title
