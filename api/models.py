from django.db import models


class Parking(models.Model):
    name = models.CharField(verbose_name='Название парковочного места', max_length=80, unique=True)

    def __str__(self):
        return self.name


class ParkingDetail(models.Model):
    parking = models.ForeignKey(Parking, verbose_name='Парковочное место', on_delete=models.CASCADE)
    arrival = models.DateTimeField(verbose_name='Время прибытия')
    departure = models.DateTimeField(verbose_name='Время отъезда')

    class Meta:
        ordering = ['-arrival']
        unique_together = ('parking', 'arrival', 'departure')
