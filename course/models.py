from django.db import models

# Create your models here.


class CourseInfo(models.Model):
    title = models.CharField(max_length=500)
    initial_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True,null=True)  # dastlabki narx
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # salary_middle=models.CharField(max_length=500)
    # contract_number = models.PositiveIntegerField(blank=True, null=True)
    monthly_duration = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)



    def total_price(self):
        return self.price * self.monthly_duration


#
# class CourseModule(models.Model):
#     course = models.ForeignKey(
#         CourseInfo,
#         on_delete=models.CASCADE,
#         related_name='modules'
#     )
#     title = models.CharField(max_length=255)
#     # description = models.TextField(blank=True)
#
#     def __str__(self):
#         return f"{self.course.title} - {self.title}"




