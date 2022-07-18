from django.shortcuts import render,redirect
from .models import Wishlist
from store .models import Product
from multiprocessing import context
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = 'login')
def wish_list(request):
    wish_list = Wishlist.objects.filter(user=request.user)
    context={
        'wish_list': wish_list
    }
    return render(request, 'store/wishlist.html',context)

@login_required(login_url = 'login')
def add_to_wishlist(request,id):
   product = Product.objects.get(id =id)
   if request.user.is_authenticated:
        try:
            wish_list = Wishlist.objects.get(product=product,user=request.user)
           
            wish_list.save()
        except Wishlist.DoesNotExist:
            wish_list = Wishlist.objects.create(
                product = product,
                user = request.user,
            )
            wish_list.save()
   else:
        try:
            wish_list= Wishlist.objects.get(product=product)
            wish_list.save()
        except Wishlist.DoesNotExist:
            wish_list = Wishlist.objects.create(
                product = product,
                
            )
            wish_list.save()  
   return redirect('wish_list')



def remove_wishlist(request,id):
    product = Wishlist.objects.get(product_id=id)
    product.delete()
    return redirect('wish_list')