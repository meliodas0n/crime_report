from django.db import models

# Create your models here.
class Complaint(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phonenumber = models.AutoField(primary_key = True)
    subject = models.CharField(max_length = 50)
    description = models.TextField()
    
    def __str__(self):
        return self.name