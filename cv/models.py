from django.db import models

class Education(models.Model):
    start_year = models.IntegerField(default=0)
    end_year = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}, {self.organization}'

class Technologies(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Cv(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    information = models.TextField(default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=50, default='')
    github = models.URLField(default='')
    linkedin = models.URLField(default='')
    technologies = models.ManyToManyField(Technologies)
    education = models.ManyToManyField(Education)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
