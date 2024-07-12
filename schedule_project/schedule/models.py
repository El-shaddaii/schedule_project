from django.db import models

class Event(models.Model):
    DAY_CHOICES = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday'),
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES)
    start_hour = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()  # Duration in hours

    def __str__(self):
        return f"{self.day} {self.start_hour}:00 for {self.duration} hour(s)"
