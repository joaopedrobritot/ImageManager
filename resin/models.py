from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Calculator(models.Model):
    your_resin = models.PositiveIntegerField()
    target_resin = models.PositiveIntegerField()

    def __str__(self):
        return 'Resin Calculator'