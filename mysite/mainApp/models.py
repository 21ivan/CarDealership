from django.db import models


def upload_location(instance, filename):
    return f'{instance.id}, {filename}'


class Info(models.Model):
    title = models.CharField(max_length=170)
    content = models.TextField(max_length=900)

    def __str__(self):
        return self.title


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name


class Car(models.Model):
    model = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    year = models.DateField()
    capacity = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=100)
    car_type = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              height_field='height_field',
                              width_field='width_field'
                              )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    brand = models.ForeignKey(Brand,
                              on_delete=models.CASCADE,
                              blank=True,
                              null=True
                              )

    def __str__(self):
        return self.model
