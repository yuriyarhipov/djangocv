# Generated by Django 3.0.4 on 2020-04-09 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_education_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cv.Organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='website',
            field=models.URLField(blank=True, default=''),
        ),
    ]