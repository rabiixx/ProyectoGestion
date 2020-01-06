# Generated by Django 2.2.6 on 2020-01-05 19:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreTest', models.CharField(max_length=30, unique=True)),
                ('co2_agua', models.FloatField(default=0)),
                ('co2_vehiculo', models.FloatField(default=0)),
                ('co2_edificios', models.FloatField(default=0)),
                ('co2_electricidad', models.FloatField(default=0)),
                ('co2_calefaccion', models.FloatField(default=0)),
                ('co2_personal', models.FloatField(default=0)),
                ('co2_viajes', models.FloatField(default=0)),
                ('co2_generacion', models.FloatField(default=0)),
                ('co2_total', models.FloatField(default=0)),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ViajesEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroViajes', models.IntegerField()),
                ('distanciaMedia', models.IntegerField()),
                ('nombreTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TestUsuario')),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TablaConstantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cons_agua', models.FloatField(default=1.5)),
                ('cons_edificios', models.FloatField(default=1.5)),
                ('cons_electricidad', models.FloatField(default=1.5)),
                ('cons_calefaccion', models.FloatField(default=1.5)),
                ('cons_personal', models.FloatField(default=1.5)),
                ('cons_viajes', models.FloatField(default=1.5)),
                ('cons_generacion', models.FloatField(default=1.5)),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroPersonal', models.IntegerField()),
                ('nombreTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TestUsuario')),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GeneracionElectricidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadGenerada', models.FloatField()),
                ('tipo', models.CharField(choices=[('Paneles Solares', 'Paneles Solares'), ('Minieolica', 'Minieolica')], default='Paneles Solares', max_length=100)),
                ('nombreTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TestUsuario')),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumoVehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoVehiculo', models.CharField(choices=[('anyCar', 'Coche'), ('anyFlight', 'Avión'), ('bus', 'Autobús'), ('taxi', 'Taxi'), ('transitRail', 'Tren'), ('motorbike', 'Moto')], default='Coche', max_length=100)),
                ('kilometrosSemana', models.IntegerField()),
                ('tipoCombustible', models.CharField(choices=[('motorGasoline', 'Gasolina'), ('diesel', 'Diesel'), ('aviationGasoline', 'Gasolina Aviacion'), ('jetFuel', 'Jet Fuel')], default='Gasolina', max_length=100)),
                ('nombreTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TestUsuario')),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumoElectricidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kwHora', models.FloatField()),
                ('nombreTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TestUsuario')),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumoEdificios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroEdificios', models.IntegerField()),
                ('tipoEdificio', models.CharField(choices=[('Cemento', 'Cemento'), ('Madera', 'Madera'), ('Acero', 'Acero')], default='Cemento', max_length=100)),
                ('nombreTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TestUsuario')),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumoCalefaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Gas Natural', 'Gas Natural'), ('Eléctrico', 'Eléctrico'), ('Carbón', 'Carbón'), ('Gasóleo', 'Gasóleo')], default='Gas Natural', max_length=100)),
                ('gasto', models.IntegerField()),
                ('nombreTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TestUsuario')),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumoAgua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('litrosAgua', models.IntegerField()),
                ('nombreTest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.TestUsuario')),
                ('nombreUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
