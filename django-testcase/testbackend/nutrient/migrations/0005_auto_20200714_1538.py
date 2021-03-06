# Generated by Django 3.0.8 on 2020-07-14 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrient', '0004_feed_standard'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutrient',
            name='standard',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='기준량(g)'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='standard',
            field=models.CharField(blank=True, default='', max_length=1000, null=True, verbose_name='기준량(g)'),
        ),
    ]
