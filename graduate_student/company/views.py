from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Company
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

@login_required
def company_storage(request):
    query = request.GET.get('q')
    if query:
        all_objects = Company.objects.filter(name__icontains=query).order_by('name')
    else:
        all_objects = Company.objects.all().order_by('name')

    paginator = Paginator(all_objects, 10)  # Разбиваем на страницы, по 10 объектов на каждой странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'company/company_list.html', {'page_obj': page_obj})


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_details.html'
    context_object_name = 'article'