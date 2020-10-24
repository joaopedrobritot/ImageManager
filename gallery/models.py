from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery') # mudar o upload no firebase
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title