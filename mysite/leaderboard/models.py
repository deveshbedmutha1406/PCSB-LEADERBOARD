from django.db import models

# Create your models here.

# to store member information

class Leader(models.Model):
    name = models.CharField(max_length=200)     #name field
    points = models.IntegerField()

    def __str__(self):
        return self.name

# table to store attendace file.
class Attendace(models.Model):
    file = models.FileField()
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name