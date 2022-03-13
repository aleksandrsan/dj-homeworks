from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=50, verbose_name='Наименование')
    discription = models.CharField(max_length=200, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name

class Measurement(models.Model):

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, verbose_name='Датчик', related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'

    def __str__(self):
        return f'{self.sensor.name}'