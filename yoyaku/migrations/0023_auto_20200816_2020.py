# Generated by Django 3.0.7 on 2020-08-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku', '0022_myuser_stripecustomerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='stripeProductId',
            field=models.CharField(max_length=300, null=True, verbose_name='stripe product id'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='stripeSubscriptionId',
            field=models.CharField(max_length=300, null=True, verbose_name='stripe subscription id'),
        ),
    ]
