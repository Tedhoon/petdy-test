# Generated by Django 3.0.8 on 2020-08-11 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datas', '0007_agerange_caution_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='a',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='피부(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='b',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='관절(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='c',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='눈(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='d',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='심장(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='e',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='신장(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='f',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='방광(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='g',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='치아(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='h',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='간(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='i',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='췌장염(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='j',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='종양(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='k',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='비타민결핍(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='l',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='면역력결핍(위험도 %)'),
        ),
        migrations.AddField(
            model_name='disease',
            name='m',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='칼슘결핍(위험도 %)'),
        ),
    ]
