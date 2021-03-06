# Generated by Django 3.0.7 on 2020-10-18 20:51

from django.db import migrations, models
from django.utils.crypto import get_random_string


def create_referral_code(apps, schema_editor):
    MyUser = apps.get_model('yoyaku', 'MyUser')
    for user in MyUser.objects.all():
        user.referral_code = get_random_string(length=8)
        user.save(update_fields=['referral_code'])


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku', '0027_myuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='referral_code',
            field=models.CharField(max_length=8, unique=True, verbose_name='referral code', blank=True, null=True),
            preserve_default=False,
        ),
        migrations.RunPython(create_referral_code),
        migrations.AlterField(
            model_name='myuser',
            name='referral_code',
            field=models.CharField(max_length=8, unique=True, verbose_name='referral code'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.CharField(blank=True, choices=[('bear', 'Bear'), ('cat', 'Cat'), ('deer', 'Deer'), ('dog', 'Dog'), ('fox', 'Fox'), ('giraffe', 'Giraffe'), ('gorilla', 'Gorilla'), ('koala', 'Koala'), ('llama', 'Llama'), ('panda', 'Panda'), ('pug', 'Pug'), ('rabbit', 'Rabbit'), ('raccoon', 'Raccoon'), ('reindeer', 'Reindeer'), ('skunk', 'Skunk'), ('wolf', 'Wolf'), ('lion', 'Lion'), ('weasel', 'Weasel'), ('monkey', 'Monkey'), ('pig', 'Pig')], max_length=10, verbose_name='avatar'),
        ),
    ]
