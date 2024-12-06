# Generated by Django 5.0.6 on 2024-06-27 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employmenthistory',
            options={'verbose_name': 'Трудовая выпускника', 'verbose_name_plural': 'Трудовые выпускников'},
        ),
        migrations.AlterModelOptions(
            name='graduate',
            options={'verbose_name': 'Выпускника', 'verbose_name_plural': 'Выпускники'},
        ),
        migrations.AddField(
            model_name='employmenthistory',
            name='employment_placework',
            field=models.CharField(default='Безработный', max_length=200, verbose_name='Место работы'),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='change_date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='employmenthistory',
            name='employment_status',
            field=models.CharField(max_length=40, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='address',
            field=models.CharField(max_length=200, verbose_name='Адрес проживания'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='citizenship',
            field=models.CharField(max_length=100, verbose_name='Гражданство'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='date_of_birth',
            field=models.DateField(verbose_name='Дата Рождения'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='education_form',
            field=models.CharField(choices=[('Full-time', 'Очная'), ('Part-time', 'Заочная')], max_length=20, verbose_name='Форма обучения'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='employment_book',
            field=models.BooleanField(verbose_name='Наличие трудовой книжки'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='enrollment_year',
            field=models.IntegerField(verbose_name='Год поступления'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='full_name',
            field=models.CharField(max_length=100, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='gender',
            field=models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='graduation_year',
            field=models.IntegerField(verbose_name='Год окончания'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='phone_number',
            field=models.CharField(max_length=15, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='snils',
            field=models.CharField(max_length=20, verbose_name='СНИЛС'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='study_direction_code',
            field=models.CharField(max_length=20, verbose_name='Код направления подготовки'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='study_direction_name',
            field=models.CharField(max_length=200, verbose_name='Название направления подготовки'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='study_direction_profile',
            field=models.CharField(max_length=200, verbose_name='Профиль направления подготовки'),
        ),
    ]
