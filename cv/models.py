from django.db import models

class Education(models.Model):
    start_year = models.IntegerField(default=0)
    end_year = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    website = models.URLField(default='')

    def __str__(self):
        return self.title


class Technologies(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Experience(models.Model):
    start_year = models.IntegerField(default=0)
    end_year = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    website = models.URLField(default='', blank=True)

    def __str__(self):
        return f'{self.start_year}-{self.end_year} {self.title} ({self.company_name})'

class Points(models.Model):
    title = models.TextField(default='')
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, default=None)

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
    experience = models.ManyToManyField(Experience)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
