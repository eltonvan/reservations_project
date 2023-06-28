# Generated by Django 4.2.2 on 2023-06-28 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('date_contract', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('kundennummer', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=255)),
                ('login', models.URLField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('booking_day', models.DateField()),
                ('num_guests', models.IntegerField()),
                ('fname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('purpose', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('t_sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('commission', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rech_num', models.CharField(max_length=255)),
                ('link_reservation', models.URLField()),
                ('guest_document', models.FileField(upload_to='guest_documents/')),
                ('link', models.URLField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.apartment')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.platform')),
            ],
        ),
    ]
