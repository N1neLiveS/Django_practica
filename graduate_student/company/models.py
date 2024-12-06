from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Название предприятия')
    address = models.CharField(max_length=200, verbose_name='Адрес предприятия')
    inn = models.CharField(max_length=12, verbose_name='ИНН предприятия')
    okved = models.CharField(max_length=30, verbose_name='ОКВЭД предприятия')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона предприятия')
    email = models.EmailField(verbose_name='E-mail предприятия')
    website = models.URLField(max_length=200, verbose_name='Сайт предприятия')

    def __str__(self):
        return self.name if self.name else 'No Name'

    class Meta:
        verbose_name = 'Предприятие'
        verbose_name_plural = 'Предприятия'
