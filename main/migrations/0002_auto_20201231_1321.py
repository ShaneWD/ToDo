# Generated by Django 3.1 on 2020-12-31 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='notes',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=24),
        ),
    ]
