# Generated by Django 3.0.7 on 2021-01-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku', '0029_studentprofile_should_pay_signup_fee'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('link', models.CharField(max_length=200, verbose_name='link')),
                ('meeting_id', models.CharField(max_length=200, verbose_name='meeting id')),
                ('password', models.CharField(max_length=200, verbose_name='password')),
            ],
        ),
    ]