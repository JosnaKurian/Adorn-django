from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth
from store .models import Category, Sub_Category, Product, ReviewRating
from unicodedata import category
from multiprocessing import context
from accounts .models import Account
from django.db.models import Q
from .forms import CategoryForm, Sub_CategoryForm, ProductForm, OrderForm
from django.template.defaultfilters import slugify
from orders .models import Order, OrderProduct
from django.contrib.auth.decorators import login_required


# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email,password=password)
        
        if user.is_superadmin == True:
              request.session['email']=email
              return redirect(dashboard)
        else:
             messages.error(request,'Invalid entry!')
             return redirect(admin_login)
    else:
        return render(request,'admin_panel/admin_login.html')


@login_required(login_url = 'admin_login')
def dashboard(request):
    return render(request,'admin_panel/dashboard.html')


def categories(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            category = Category.objects.filter(Q(category_name__icontains=keyword))
        if not category.exists():
            messages.error(request,'No matching item found.')
            return redirect(request,'admin_panel/categories.html')
    else:
        category = Category.objects.all().order_by('category_name')
    context ={
       'Category': category,
    }
    return render(request,'admin_panel/categories.html',context)


def add_categories(request):
    form = CategoryForm
    try:
        if request.method =='POST':
            form = CategoryForm(request.POST,request.FILES)
            if form.is_valid():
                cat_name = form.cleaned_data['category_name']
                slug = slugify(cat_name)
                category = form.save()
                category.slug = slug
                category.save()
                return redirect('categories')
        return render(request,'admin_panel/add_category.html',{'form':form})
    except:
        messages.error(request,'slug already exists')
        return redirect(request,'add_categories')


def edit_categories(request,slug):
    category = Category.objects.get(slug=slug)
    form = CategoryForm(instance=category)
    try:
        if request.method == 'POST':
            form = CategoryForm(request.POST,request.FILES,instance=category)
            if form.is_valid():
                form.save()
                return redirect('categories')      
    except:
        messages.error(request,"Slug already exists")
        return redirect('edit_categories')  
    context = {
        'category' :category,
        'form' : form
    }                     
    return render(request,'admin_panel/edit_category.html',context)


def delete_categories(request,id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('categories')
   

def sub_categories(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            sub_category = Sub_Category.objects.filter(Q(sub_category_name__icontains=keyword))
        if not sub_category.exists():
            messages.error(request,'No matching item found.')
            return redirect(request,'admin_panel/sub_categories.html')
    else:
        sub_category = Sub_Category.objects.all()
    context ={

       'Sub_Category': sub_category,
    }
    return render(request,'admin_panel/sub_categories.html',context)


def add_subcategories(request):
    form = Sub_CategoryForm
    try:
        if request.method =='POST':
            form = Sub_CategoryForm(request.POST)
            if form.is_valid():
                subcat_name = form.cleaned_data['sub_category_name']
                slug = slugify(subcat_name)
                sub_category = form.save()
                sub_category.slug = slug
                sub_category.save()
                return redirect('sub_categories')
        return render(request,'admin_panel/add_subcategory.html',{'form':form})
    except:
        messages.error(request,'slug already exists')
        return redirect(request,'add_subcategories')


def edit_subcategories(request,slug):
    sub_category = Sub_Category.objects.get(slug=slug)
    form = Sub_CategoryForm(instance=sub_category)
    try:
        if request.method == 'POST':
            form = Sub_CategoryForm(request.POST,request.FILES,instance=sub_category)
            if form.is_valid():
                form.save()
                return redirect('sub_categories')      
    except:
        messages.error(request,"Slug already exists")
        return redirect('edit_subcategories')  
    context = {
        'sub_category' : sub_category,
        'form' : form
    }                     
    return render(request,'admin_panel/edit_subcategory.html',context)


def delete_subcategories(request,id):
    sub_category = Sub_Category.objects.get(id=id)
    sub_category.delete()
    return redirect('sub_categories')


def products(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product = Product.objects.order_by('product_name').filter(Q(product_name__icontains=keyword))
        if not product.exists():
            messages.error(request,'No matching item found.')
            return redirect(request,'admin_panel/products.html')
    else:
        product = Product.objects.all()
    context ={
       
        'Product' : product,
    }
    return render(request,'admin_panel/products.html',context)


def add_products(request):
    form = ProductForm
    try:
        if request.method =='POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                productname = form.cleaned_data['product_name']
                slug = slugify(productname)
                product = form.save()
                product.slug = slug
                
                images = request.FILES.getlist('images')
                for image in images:
                    ProductGallery.objects.create(
                        image=image,
                        product = product, #add images using for loop in list
                )
                images.save()
                product.save()
                return redirect('products')
        return render(request,'admin_panel/add_product.html',{'form':form})
    except:
        messages.error(request,'slug already exists')
        return redirect(request,'add_products')


def edit_products(request,slug):
    product = Product.objects.get(slug=slug)
    form = ProductForm(instance=product)
    try:
        if request.method == 'POST':
            form = ProductForm(request.POST,request.FILES,instance=product)
            if form.is_valid():
                form.save()
                return redirect('products')      
    except:
        messages.error(request,"Slug already exists")
        return redirect('edit_products')  
    context = {
        'product' :product,
        'form' : form
    }                     
    return render(request,'admin_panel/edit_product.html',context)


def delete_products(request,id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('products')


def customers(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            customer = Account.objects.filter(Q(first_name__icontains=keyword) | Q(last_name__icontains=keyword))
        if not customer.exists():
            messages.error(request,'No matching item found.')
            return redirect(request,'admin_panel/customers.html')
    else:
        customer = Account.objects.filter(is_superadmin = False).order_by('-id')
    context ={

       'Account': customer,
    }
    return render(request,'admin_panel/customers.html',context)
    

def block_user(request, id):
    account = Account.objects.get(id=id)
    if account.is_active:
        account.is_active = False
        account.save()    
    else :
        account.is_active = True
        account.save()
    return redirect('customers')   



def orders(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            order = Order.objects.filter(Q(first_name__icontains=keyword))
        if not order.exists():
            messages.error(request,'No matching item found.')
            return redirect(request,'admin_panel/order.html')
    else:
        order = Order.objects.all()
    context ={

       'Order': order,
    }
    return render(request,'admin_panel/order.html',context)

def update_orders(request,id):
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)
    try:
        if request.method == 'POST':
            form = OrderForm(request.POST,request.FILES,instance=order)
            if form.is_valid():
                form.save()
                return redirect('orders')      
    except:
        messages.error(request,"Slug already exists")
        return redirect('update_orders')  
    context = {
        'Order' :order,
        'form' : form
    }                     
    return render(request,'admin_panel/update_order.html',context)

def order_details(request,id):
    order = Order.objects.get(id=id)
    context={
        'Order' :order,
    }
    return render(request,'admin_panel/order_details.html',context)


def Review_Rating(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            reviewRating = ReviewRating.objects.filter(Q(first_name__icontains=keyword))
        if not reviewRating.exists():
            messages.error(request,'No matching item found.')
            return redirect(request,'admin_panel/ReviewRating.html')
    else:
        reviewRating = ReviewRating.objects.all()
    context ={

       'ReviewRating': reviewRating,
    }
    return render(request,'admin_panel/ReviewRating.html',context)


def delete_Review_Rating(request,id):
    reviewRating = ReviewRating.objects.get(id=id)
    reviewRating.delete()
    return redirect('Review_Rating')