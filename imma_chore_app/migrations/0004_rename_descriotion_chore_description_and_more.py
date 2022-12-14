# Generated by Django 4.1.4 on 2023-01-06 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imma_chore_app', '0003_remove_chore_day_of_the_week_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chore',
            old_name='descriotion',
            new_name='description',
        ),
        migrations.AddField(
            model_name='chore',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 1, 6, 15, 36, 29, 76910, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kid',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 1, 6, 15, 36, 55, 154625, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kid_chore',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 1, 6, 15, 37, 4, 604099, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kid_chore',
            name='day_of_the_week',
            field=models.CharField(max_length=12),
        ),
    ]
