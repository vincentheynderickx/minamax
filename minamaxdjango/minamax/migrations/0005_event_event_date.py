# Generated by Django 5.0 on 2024-01-09 13:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minamax', '0004_remove_bet_number_remove_possibility_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date event'),
            preserve_default=False,
        ),
    ]