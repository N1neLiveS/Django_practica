from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import DetailView
from django.http import HttpResponse
from .models import Graduate, EmploymentHistory
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
import textwrap
from django.contrib.auth.decorators import login_required

@login_required
def student_storage(request):
    query = request.GET.get('q')
    if query:
        all_objects = Graduate.objects.filter(full_name__icontains=query).order_by('full_name')
    else:
        all_objects = Graduate.objects.all().order_by('full_name')

    paginator = Paginator(all_objects, 10)  # Разбиваем на страницы, по 10 объектов на каждой странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'students/persons.html', {'page_obj': page_obj})


class PersonDetailView(DetailView):
    model = Graduate
    template_name = 'students/details_view.html'
    context_object_name = 'graduate'

@login_required
def personal_details(request, pk):
    graduate = get_object_or_404(Graduate, pk=pk)
    return render(request, 'students/personal_details.html', {'graduate': graduate})

@login_required
def employment_details(request, pk):
    graduate = get_object_or_404(Graduate, pk=pk)
    employment_history = EmploymentHistory.objects.filter(graduate=graduate)
    return render(request, 'students/employment_details.html', {'graduate': graduate, 'employment_history': employment_history})


@login_required
def export_to_pdf(request, pk):
    graduate = get_object_or_404(Graduate, pk=pk)
    employment_history = EmploymentHistory.objects.filter(graduate=graduate).order_by('change_date')

    # Создание PDF-файла
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    # Регистрация шрифта, поддерживающего кириллицу
    pdfmetrics.registerFont(TTFont('Arial-Bold', 'Arial-Bold.ttf'))
    pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

    # Загрузка изображения для фона
    background_image = ImageReader('pdf_background.jpg')

    # Получение размеров страницы
    width, height = A4

    # Рисование фона
    pdf.drawImage(background_image, 0, 0, width=width, height=height)

    # Установка начальной позиции по вертикали
    y_position = 800  # Начальная позиция по вертикали, учитывая размер страницы A4

    # Заполнение PDF-файла данными о студенте
    data = [
        ('ФИО', graduate.full_name),
        ('Дата рождения', graduate.date_of_birth),
        ('Пол', graduate.gender),
        ('Гражданство', graduate.citizenship),
        ('Адрес проживания', graduate.address),
        ('Телефон', graduate.phone_number),
        ('Электронная почта', graduate.email),
        ('СНИЛС', graduate.snils),
        ('Код направления подготовки', graduate.study_direction_code),
        ('Название направления подготовки', graduate.study_direction_name),
        ('Профиль направления подготовки', graduate.study_direction_profile),
        ('Год поступления', graduate.enrollment_year),
        ('Год окончания', graduate.graduation_year),
        ('Форма обучения', graduate.education_form)
    ]

    max_width = 500  # Максимальная ширина строки

    for label, value in data:
        # Рисуем заголовок жирным шрифтом
        pdf.setFont("Arial-Bold", 12)
        label_text = f'{label}: '
        pdf.drawString(50, y_position, label_text)

        # Определяем позицию для значения
        text_width = pdf.stringWidth(label_text, "Arial-Bold", 12)

        # Разбиваем значение на строки
        wrapped_text = textwrap.wrap(str(value), width=(max_width - text_width) // 8)

        pdf.setFont("Arial", 12)
        for line in wrapped_text:
            pdf.drawString(50 + text_width, y_position, line)
            y_position -= 10  # уменьшаем позицию по вертикали для следующей строки

        y_position -= 20  # дополнительный отступ между записями

    y_position -= 40
    # Заполнение PDF-файла трудовой историей выпускника
    pdf.setFont("Arial-Bold", 14)
    pdf.drawString(50, y_position, "Трудовая история:")
    y_position -= 30  # отступ перед трудовой историей

    pdf.setFont("Arial", 12)
    for record in employment_history:
        company_name = record.employment_placework.name if record.employment_placework else "Поставлен на учёт"
        employment_line = f'{record.change_date} - {company_name} - {record.employment_status}'

        # Разбиваем строку на несколько, если она слишком длинная
        wrapped_text = textwrap.wrap(employment_line, width=max_width // 8)

        for line in wrapped_text:
            pdf.drawString(50, y_position, line)
            y_position -= 10  # уменьшаем позицию по вертикали для следующей строки

        y_position -= 20  # дополнительный отступ между записями трудовой истории

    pdf.showPage()
    pdf.save()

    buffer.seek(0)

    # Отправка PDF в HTTP response
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{graduate.full_name}_details.pdf"'

    return response
