from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class UserPredictDataModel(models.Model):
    pH = models.CharField(max_length=100)
    Temperature = models.CharField(max_length=100)
    Taste = models.CharField(max_length=100)
    Odour = models.CharField(max_length=100)
    Fat = models.CharField(max_length=100)
    Turbidity = models.CharField(max_length=100)
    Colour = models.CharField(max_length=100)
    Grade = models.CharField(max_length=100)


def __str__(self):
    return self.pH, self.Temperature,self.Taste,self.Odour,self.Fat,self.Turbidity,self.Colour,self.Grade

class FeedModel(models.Model):
    Feedback = models.TextField(max_length=100)

    def __str__(self):
        return str(self.Feedback)