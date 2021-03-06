# Generated by Django 2.2.7 on 2020-08-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrient', '0007_auto_20200714_1719'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangedSnack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='간식 이름')),
                ('calorie', models.CharField(max_length=1000, verbose_name='칼로리(kcal)')),
                ('moisture', models.CharField(max_length=1000, verbose_name='수분량(ml)')),
                ('crude_protein', models.CharField(max_length=1000, verbose_name='조단백(g)')),
                ('crude_fat', models.CharField(max_length=1000, verbose_name='조지방(g)')),
                ('crude_fiber', models.CharField(max_length=1000, verbose_name='조섬유(g)')),
                ('crude_ash', models.CharField(max_length=1000, verbose_name='조회분(g)')),
                ('calcium', models.CharField(max_length=1000, verbose_name='칼슘(g)')),
                ('phosphorus', models.CharField(max_length=1000, verbose_name='인(g)')),
            ],
            options={
                'verbose_name': '간식 환산 - [1g당 성분양]',
                'verbose_name_plural': '간식 환산- [1g당 성분양]',
            },
        ),
        migrations.DeleteModel(
            name='Snack',
        ),
        migrations.AlterField(
            model_name='exchangedfeed',
            name='moisture',
            field=models.CharField(max_length=1000, verbose_name='수분량(ml)'),
        ),
        migrations.AlterField(
            model_name='exchangednutrient',
            name='moisture',
            field=models.CharField(max_length=1000, verbose_name='수분량(ml)'),
        ),
    ]
