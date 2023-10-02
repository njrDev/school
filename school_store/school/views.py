from django.shortcuts import render,redirect
from django.http import JsonResponse

from .models import Category,Subcategory,Product


# Create your views here.

def index(request):
    return render(request, "index.html")

def add_product(request):
    categories = Category.objects.all()
    context = {
        "categories":categories,
    }
    if request.method == "POST":
        return redirect('confirm')
    return render(request,'add_product.html',context)

def get_subcategories(request, category_id):
    category = Category.objects.get(id=category_id)
    subcategories = list(category.subcategories.all().values())
    return JsonResponse(subcategories, safe=False)

def confirm(request):
    return render(request, 'confirm.html')