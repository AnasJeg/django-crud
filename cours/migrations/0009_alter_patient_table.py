# Generated by Django 4.0.4 on 2023-04-03 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0008_alter_patient_type'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='patient',
            table='patientdb',
        ),
    ]