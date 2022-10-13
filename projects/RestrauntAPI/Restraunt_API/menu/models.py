from django.db import models
import datetime


def upload_to(instance, filename):
    return f"posts/{filename}".format(filename=filename)


# Create your models here.
class Menu(models.Model):
    Item_name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to=upload_to, default="")
    Category = models.CharField(max_length=50)
    Price = models.FloatField()
    Discount = models.FloatField()
    Plate_size = models.IntegerField()

    def __str__(self):
        return self.Item_name


class Order(models.Model):
    user = models.EmailField(verbose_name="email", max_length=60, unique=False)
    Item_name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to=upload_to, default="")
    Price = models.FloatField()
    Discount = models.FloatField()
    Plate_size = models.IntegerField()
    zip_code = models.IntegerField()
    Address = models.TextField()
    ord_date = models.DateTimeField(default=datetime.datetime.now())
    sts = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.Item_name
