# Generated by Django 3.0.4 on 2020-05-25 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku', '0016_auto_20200515_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='file',
            field=models.FileField(null=True, upload_to='hsw14yh841sr/public/media/eventFiles/'),
        ),
    ]
