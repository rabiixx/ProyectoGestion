# Generated by Django 2.2.6 on 2020-01-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200105_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumovehiculo',
            name='tipoVehiculo',
            field=models.CharField(choices=[('anyCar', 'Coche'), ('anyFlight', 'Avión'), ('bus', 'Autobús'), ('taxi', 'Taxi'), ('transitRail', 'Tren'), ('motorbike', 'Moto')], default='Coche', max_length=100),
        ),
    ]
