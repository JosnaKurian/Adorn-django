from django.shortcuts import render
from store.models import Category

# Create your views here.
def home(request):
    # products = Product.objects.all().filter(is_available=True)

    # context = { 'products': products, }
    categories = Category.objects.all()

    context = { 'categories': categories, }

    return render(request,'index.html',context)


