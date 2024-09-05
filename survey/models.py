from django.db import models

class NearMiss(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    encounters = models.PositiveIntegerField()
    prevention = models.TextField()

    def __str__(self):
        return self.title
