from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=False)
    place = models.TextField(blank=False)
    description = models.TextField(blank=False)
    date_enrolled = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.name