from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_location = models.CharField(max_length=100)
    event_description = models.TextField()

    def __str__(self):
        return self.event_name
