from django.shortcuts import render, redirect
from students.models import Graduate
from company.models import Company
from students.forms import GraduateForm, HistoryForm
from company.forms import CompanyForm
from django.contrib.auth.decorators import login_required
from .forms import CSVUploadForm
import csv
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required
def create_choice(request):
    return render(request, 'create/create_choice.html')

@login_required
def student_create(request):
    if request.method == 'POST':
        form = GraduateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = GraduateForm()
    return render(request, 'create/student_create.html', {'form': form})

@login_required
def history_create(request):
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = HistoryForm()
    return render(request, 'create/history_create.html', {'form': form})

@login_required
def company_create(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company')
    else:
        form = CompanyForm()
    return render(request, 'create/company_create.html', {'form': form})

def success_url(request):
    return render(request, 'create/success.html')

def error_url(request):
    return render(request, 'create/error_csv.html')

@login_required
def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            model_name = form.cleaned_data['model_name']
            csv_file = form.cleaned_data['csv_file']
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                reader = csv.reader(decoded_file)
                if model_name == 'Graduate':
                    model = Graduate
                elif model_name == 'Company':
                    model = Company
                else:
                    return HttpResponseRedirect(reverse('error'))  # Перенаправление на страницу с ошибкой, если модель не найдена
                field_names = [field.name for field in model._meta.fields if field.name != 'id']
                next(reader)
                for row in reader:
                    if len(row) != len(field_names):
                        return HttpResponseRedirect(reverse('error'))  # Перенаправление на страницу с ошибкой, если количество полей не совпадает
                    try:
                        data = {field_names[i]: row[i] for i in range(len(row))}
                        model.objects.create(**data)
                    except Exception as e:
                        return HttpResponseRedirect(reverse('error'))  # Перенаправление на страницу с ошибкой при любом исключении
                return HttpResponseRedirect(reverse('success'))  # Перенаправление на страницу с успешной загрузкой
            except Exception as e:
                return HttpResponseRedirect(reverse('error'))  # Перенаправление на страницу с ошибкой при возникновении любого исключения при чтении CSV
    else:
        form = CSVUploadForm()
    return render(request, 'create/upload.html', {'form': form})