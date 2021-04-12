from django.db import models


class djangoClasses(models.Model)
    Title =models.CharField(max_length=70)
    Course_Number = models.DecimalField(default=0.00, max_digits=5000,decimal_places=3)
    Instructor_Name= models.TextField(max_length=400, default="", blank=True)
    Duration = models.DurationField()

# Create your models here.
