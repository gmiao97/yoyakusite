# Generated by Django 3.0.4 on 2020-04-26 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku', '0013_event_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='file',
            field=models.FileField(null=True, upload_to='eventFiles/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='comment',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='comment'),
        ),
    ]
