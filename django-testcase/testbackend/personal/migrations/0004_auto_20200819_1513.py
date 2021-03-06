# Generated by Django 3.0.8 on 2020-08-19 06:13

from django.db import migrations, models
import personal.models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_mypet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypet',
            name='image',
            field=models.ImageField(default='mypet_images/default/dog.jpg', upload_to=personal.models.get_mypet_image_filename, verbose_name='반려동물 이미지'),
        ),
    ]
