from django.db import models

# Create your models here.


class CourseInfo(models.Model):
    title = models.CharField(max_length=500)
    duration = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    salary_middle=models.CharField(max_length=500)

    def total_price(self):
        return self.price * self.duration

