# Generated by Django 2.2.7 on 2020-07-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrient', '0003_auto_20200714_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='standard',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='기준량'),
        ),
    ]
