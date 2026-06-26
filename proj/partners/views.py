from django.shortcuts import render
from .models import Category

def dashboard_view(request):
    categories = Category.objects.prefetch_related('offers').all()
    return render(request, 'dashboard.html', {'categories': categories})