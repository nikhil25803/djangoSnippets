# Generated by Django 3.2.9 on 2022-02-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='dou',
        ),
        migrations.RemoveField(
            model_name='project',
            name='year',
        ),
        migrations.AlterField(
            model_name='project',
            name='lang',
            field=models.CharField(max_length=100),
        ),
    ]
