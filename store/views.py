from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Sub_Category, Product
from carts.views import _cart_id
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.contrib import messages
from .models import ReviewRating, ProductGallery
from orders.models import OrderProduct
from django.db.models import Max, Min

# Create your views here.
# def shop(request, category_slug=None, sub_category_slug=None):
#     categories = None
#     sub_categories = None
#     products = None
    
#     if category_slug != None:
#         categories = get_object_or_404(Category, slug=category_slug)
#         cat = Category.objects.all().filter(slug=category_slug)
#         products = Product.objects.filter(category=categories, is_available=True)
#         paginator = Paginator(products, 6)
#         page = request.GET.get('page')    
#         paged_products = paginator.get_page(page)

#         if sub_category_slug != None:
#            sub_categories = get_object_or_404(Sub_Category, slug=sub_category_slug)
#            products = Product.objects.filter( sub_category=sub_categories, is_available=True)
#            paginator = Paginator(products, 6)
#            page = request.GET.get('page')
#            paged_products = paginator.get_page(page)

#     else:
#         products = Product.objects.all().filter(is_available=True).order_by('id')
#         paginator = Paginator(products, 6)
#         page = request.GET.get('page')
#         paged_products = paginator.get_page(page)

#     context ={ 
#         'products': paged_products,
#         'category': categories,
#         'cat':cat,

#      }
#     return render(request,'store/category.html',context)


def shop(request, category_slug=None, sub_category_slug=None):
    categories = None
    sub_categories = None
    products = None
    
    category = get_object_or_404(Category, slug=category_slug)
    sub_cat = Sub_Category.objects.filter(category=category)
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        cat = Category.objects.all().filter(slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')    
        paged_products = paginator.get_page(page)
    
        if sub_category_slug != None:
            sub_categories = get_object_or_404(Sub_Category, slug=sub_category_slug)
            products = Product.objects.filter( sub_category=sub_categories, is_available=True)
            paginator = Paginator(products, 6)
            page = request.GET.get('page')
            paged_products = paginator.get_page(page)

    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    
        
    context ={ 
        'products': paged_products,
        'sub_cat': sub_cat,
        'category': categories,

    }
    return render(request,'store/category.html',context)


def all_products(request):
    category = Category.objects.all()
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))
    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        print(FilterPrice)
        Int_FilterPrice = int(FilterPrice)
        products = Product.objects.filter(price__lte=Int_FilterPrice)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)
 
    context ={ 
        'products': paged_products,
        'min_price': min_price,
        'max_price': max_price,
        'FilterPrice': FilterPrice,
        'category':category,
        
    }
    return render(request,'store/store.html',context)




def product_detail(request, category_slug, sub_category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,sub_category__slug=sub_category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=single_product.id).exists()
        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None

    #get the reviews
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    #Get the product gallery
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        'orderproduct':orderproduct,
        'reviews':reviews,
        'product_gallery':product_gallery,
    }
    return render(request,'store/product_detail.html',context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('created_date').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
    context ={
        'products': products,
    }
    return render(request,'store/store.html',context)


def submit_review(request, product_id):
    url=request.META.get('HTTP_REFERER')
    if request.method == "POST":
        try:
          reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
          form = ReviewForm(request.POST, instance=reviews) 
          form.save()
          messages.success(request,'Thankyou! Your review has been updated.')
          return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request,'Thankyou! Your review has been submitted.')
                return redirect(url)





