from django.db import models
from django.contrib.auth.models import User

class Travel_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    depature = models.CharField(max_length=30)
    destination = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    trip_type = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} trip"


class Packages(models.Model):
    dep = models.CharField(max_length=30)
    des = models.CharField(max_length=30)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.dep} -> {self.des}"


class Selection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_package = models.CharField(max_length=20)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} has selected {self.selected_package}"





