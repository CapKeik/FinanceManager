# Generated by Django 3.1.4 on 2020-12-13 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20201213_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='amount',
            name='date_add',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата добавления расхода'),
        ),
    ]
