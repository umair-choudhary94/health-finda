# Generated by Django 4.2.1 on 2023-07-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0005_remove_insuranceininfo_patient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='latitude',
            field=models.CharField(default='0000', max_length=100),
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='longitude',
            field=models.CharField(default='0000', max_length=100),
        ),
    ]
