# Generated by Django 3.0.8 on 2020-07-13 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrient', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feed',
            options={'verbose_name': '사료', 'verbose_name_plural': '사료'},
        ),
        migrations.AlterModelOptions(
            name='nutrient',
            options={'verbose_name': '영양제', 'verbose_name_plural': '영양제'},
        ),
        migrations.AlterModelOptions(
            name='snack',
            options={'verbose_name': '간식', 'verbose_name_plural': '간식'},
        ),
    ]
