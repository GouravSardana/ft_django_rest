# Generated by Django 3.0.6 on 2020-05-25 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200525_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityperiod',
            name='samp',
        ),
    ]
