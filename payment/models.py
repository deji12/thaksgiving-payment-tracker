from django.db import models
from cloudinary.models import CloudinaryField

class Payment(models.Model):

    name = models.CharField(max_length=200, help_text="The student's name")
    matric_number = models.CharField(max_length=20, help_text="The student's mat number")
    phone_number = models.CharField(max_length=15, help_text="The student's phone number", null=True, blank=True)
    amount = models.FloatField(default=0, help_text="The amount of money the student paid")

    part_time_student = models.BooleanField(default=False, help_text="Whether this student is a part time stuent or not")
    receipt = CloudinaryField(folder='thanksgiving-receipts/', help_text="Transaction receipt", blank=True, null=True)

    is_part_payment = models.BooleanField(default=False, help_text="Whether this is a part payment of the complete amount")
    paid_when = models.DateTimeField()

    def __str__(self):
        return self.name