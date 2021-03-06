# Generated by Django 3.0.6 on 2020-05-25 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200525_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='ftuser',
            name='user_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='endDate',
            field=models.DateTimeField(verbose_name='endDate'),
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='startDate',
            field=models.DateTimeField(verbose_name='startDate'),
        ),
        migrations.AlterField(
            model_name='ftuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
