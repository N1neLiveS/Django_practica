# Generated by Django 5.0.6 on 2024-07-02 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('students', '0004_alter_employmenthistory_employment_placework_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employmenthistory',
            name='employment_placework',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.company', verbose_name='Место работы'),
        ),
    ]
