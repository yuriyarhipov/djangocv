# Generated by Django 3.0.4 on 2020-04-09 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0010_auto_20200409_2228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='experience',
        ),
        migrations.AddField(
            model_name='experience',
            name='cv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cv.Cv'),
        ),
    ]