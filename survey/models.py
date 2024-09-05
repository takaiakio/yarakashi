from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=100)
    scene = models.TextField()
    times = models.IntegerField()
    avoid_reason = models.TextField()

    def __str__(self):
        return self.title
