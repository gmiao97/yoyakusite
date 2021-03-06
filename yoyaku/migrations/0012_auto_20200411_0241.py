# Generated by Django 3.0.4 on 2020-04-11 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yoyaku', '0011_auto_20200403_2249'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freq', models.CharField(max_length=10, verbose_name='frequency')),
                ('dtstart', models.DateTimeField(verbose_name='recurrence start')),
                ('until', models.DateTimeField(verbose_name='recurrence end')),
                ('interval', models.IntegerField(verbose_name='interval')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='isRecurrence',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='recurrence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recurrenceEvents', related_query_name='recurrenceEvent', to='yoyaku.Recurrence'),
        ),
    ]
