# Generated by Django 5.0 on 2023-12-24 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minamax', '0003_remove_event_number_alter_bet_id_alter_event_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='number',
        ),
        migrations.RemoveField(
            model_name='possibility',
            name='number',
        ),
    ]
