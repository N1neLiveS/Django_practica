# Generated by Django 5.0.6 on 2024-07-01 15:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('students', '0002_alter_employmenthistory_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmenthistory',
            name='employment_placework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
