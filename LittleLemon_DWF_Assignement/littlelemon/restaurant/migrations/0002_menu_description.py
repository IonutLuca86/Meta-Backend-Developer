# Generated by Django 5.1.4 on 2025-01-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
