from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, default='')

    def __str__(self):
        return self.name


class Education(models.Model):
    start_year = models.IntegerField(default=0)
    end_year = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True)
    cv = models.ForeignKey('Cv', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Technologies(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Experience(models.Model):
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=100)
    organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True)
    cv = models.ForeignKey('Cv', on_delete=models.SET_NULL, null=True)

    def experience_points(self):
        return Points.objects.filter(experience=self)

    def __str__(self):
        return f'{self.start_year}-{self.end_year} {self.title} ({self.organization.name})'

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

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def education(self):
        return Education.objects.filter(cv=self)

    @property
    def experience(self):
        return Experience.objects.filter(cv=self).order_by('-start_year')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
