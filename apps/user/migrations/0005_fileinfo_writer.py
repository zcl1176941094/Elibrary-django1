# Generated by Django 3.2.8 on 2022-05-19 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_dailyinfo_daily_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileinfo',
            name='writer',
            field=models.CharField(default='佚名', max_length=30, verbose_name='作者'),
        ),
    ]
