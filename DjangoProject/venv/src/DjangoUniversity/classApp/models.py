from django.db import models

# Create your models here.
class djangoClasses(models.Model):
   Title =models.CharField(max_length=70)
   Course_Number = models.DecimalField(default=0.00, max_digits=5000,decimal_places=3)
   Instructor_Name= models.TextField(max_length=400, default="", blank=True)
   Duration = models.DurationField()


   objects = models.Manager()         #create objects

   def __str__(self):
      return self.Title
