# Generated by Django 2.2.6 on 2020-01-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200105_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactoresEmision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combustible', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('factor_emision', models.FloatField()),
                ('unidad', models.CharField(default='kgCO2/l', max_length=50)),
            ],
        ),
    ]
