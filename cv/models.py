from django.db import models


class Cv(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    information = models.TextField(default='')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'