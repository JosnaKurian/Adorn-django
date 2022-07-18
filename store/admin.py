from django.contrib import admin
from .models import Category
from .models import Sub_Category
from .models import Product, ReviewRating, ProductGallery
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug':('category_name',)}
    list_display = ('category_name','slug')

admin.site.register(Category,CategoryAdmin)


class Sub_CategoryAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug':('sub_category_name',)}
    list_display = ('sub_category_name','slug')

admin.site.register(Sub_Category,Sub_CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    prepolulated_fields = {'slug':('product_name',)}
    list_display = ('product_name','price','stock','category','modified_date','is_available')
    inlines = [ProductGalleryInline]

admin.site.register(Product,ProductAdmin)

admin.site.register(ReviewRating)
admin.site.register(ProductGallery)



