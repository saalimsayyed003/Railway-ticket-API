# Generated by Django 4.0.3 on 2022-03-29 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(blank=True, max_length=50)),
                ('To', models.CharField(blank=True, max_length=50)),
                ('Departure_date', models.DateField(blank=True)),
                ('Time', models.TimeField()),
            ],
        ),
    ]
