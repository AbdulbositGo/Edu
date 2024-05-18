from django.db import models

from base.models import Student
from cources.models import Course


class Registry(models.Model):
    debit = models.DecimalField(max_digits=18, decimal_places=2)
    credit = models.DecimalField(max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.debit} | {self.credit}"
    


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registry = models.ForeignKey(Registry, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.student.first_name} paid {self.course.subject}"
    