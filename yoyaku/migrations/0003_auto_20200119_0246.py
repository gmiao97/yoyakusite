# Generated by Django 3.0.2 on 2020-01-19 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku', '0002_auto_20200119_0156'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='title', max_length=200, verbose_name='event title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(choices=[('M_JA', 'Middle School Japanese'), ('M_EN', 'Middle School English')], max_length=200, verbose_name='subject name'),
        ),
    ]
