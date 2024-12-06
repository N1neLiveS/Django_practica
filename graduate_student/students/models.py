from django.db import models
from company.models import Company

# Модель для информации о выпускнике
class Graduate(models.Model):
    full_name = models.CharField('ФИО',max_length=100)
    date_of_birth = models.DateField('Дата Рождения')
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    gender = models.CharField('Пол',max_length=1, choices=GENDER_CHOICES)
    citizenship = models.CharField('Гражданство', max_length=100)
    address = models.CharField('Адрес проживания', max_length=200)
    phone_number = models.CharField('Телефон', max_length=15)
    email = models.EmailField('Электронная почта')
    snils = models.CharField('СНИЛС', max_length=20)
    study_direction_code = models.CharField('Код направления подготовки', max_length=20)
    study_direction_name = models.CharField('Название направления подготовки', max_length=200)
    study_direction_profile = models.CharField('Профиль направления подготовки', max_length=200)
    enrollment_year = models.IntegerField('Год поступления')
    graduation_year = models.IntegerField('Год окончания')
    EDUCATION_FORM_CHOICES = [
        ('Full-time', 'Очная'),
        ('Part-time', 'Заочная'),
    ]
    education_form = models.CharField('Форма обучения',max_length=20, choices=EDUCATION_FORM_CHOICES)
    employment_book = models.BooleanField('Наличие трудовой книжки')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Выпускника'
        verbose_name_plural = 'Выпускники'

# Модель для информации о трудовой деятельности выпускника
class EmploymentHistory(models.Model):
    graduate = models.ForeignKey(Graduate, on_delete=models.CASCADE, verbose_name='Выпускник')
    employment_placework = models.ForeignKey(Company,  on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Место работы')
    employment_status = models.CharField('Должность', max_length=40, default='Безработный')
    change_date = models.DateField('Дата')

    def __str__(self):
        return f"{self.graduate.full_name} - {self.change_date}"

    class Meta:
        verbose_name = 'Трудовая выпускника'
        verbose_name_plural = 'Трудовые выпускников'