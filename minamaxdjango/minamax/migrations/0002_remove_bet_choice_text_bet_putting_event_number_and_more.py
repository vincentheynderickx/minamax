# Generated by Django 5.0 on 2023-12-24 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minamax', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bet',
            name='choice_text',
        ),
        migrations.AddField(
            model_name='bet',
            name='putting',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='event',
            name='number',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Possibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description_text', models.CharField(max_length=200)),
                ('quotation', models.FloatField(default=2.0)),
                ('number', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='minamax.event')),
            ],
        ),
        migrations.AddField(
            model_name='bet',
            name='possibility',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='minamax.possibility'),
            preserve_default=False,
        ),
    ]
