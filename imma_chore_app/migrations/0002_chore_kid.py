# Generated by Django 4.1.3 on 2023-01-04 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imma_chore_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('descriotion', models.CharField(max_length=35)),
                ('payout', models.IntegerField(blank=True, null=True)),
                ('day_of_the_week', models.DateTimeField()),
                ('is_complete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('allowance_earned', models.IntegerField(blank=True, null=True)),
                ('chore', models.ManyToManyField(to='imma_chore_app.chore')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imma_chore_app.parent')),
            ],
        ),
    ]
