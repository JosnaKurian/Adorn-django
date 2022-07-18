from django import forms
from store .models import Category, Sub_Category, Product
from orders .models import Order

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name','cat_image']

    def __init__(self,*args, **kwargs):
        super(CategoryForm,self).__init__(*args, **kwargs)

        self.fields['category_name'].widget.attrs['placeholder'] = 'Category name'
        self.fields['category_name'].widget.attrs['class'] = 'form-control'
        self.fields['category_name'].widget.attrs['type'] = 'text'


        self.fields['cat_image'].widget.attrs['type'] = 'file'
        self.fields['cat_image'].widget.attrs['class'] = 'form-control'


class Sub_CategoryForm(forms.ModelForm):
    class Meta:
        model = Sub_Category
        fields = ['category', 'sub_category_name']

    def __init__(self,*args, **kwargs):
        super(Sub_CategoryForm,self).__init__(*args, **kwargs)

        self.fields['category'].widget.attrs['placeholder'] = 'Category name'

        self.fields['sub_category_name'].widget.attrs['placeholder'] = 'Sub_Category name'
        self.fields['sub_category_name'].widget.attrs['class'] = 'form-control'
        self.fields['sub_category_name'].widget.attrs['type'] = 'text'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'sub_category', 'product_name', 'description','price','stock', 'is_available', 'images']

        widgets = {
            "primary_image":forms.ClearableFileInput(attrs={
                "class":"form-control",
                "name":"primary_image",
                "type":"file"
            })
        }

    def __init__(self,*args, **kwargs):
        super(ProductForm,self).__init__(*args, **kwargs)

        self.fields['category'].widget.attrs['placeholder'] = 'Category name'
        
        self.fields['sub_category'].widget.attrs['placeholder'] = 'Sub_Category name'
        
        self.fields['product_name'].widget.attrs['placeholder'] = 'Product name'
        self.fields['product_name'].widget.attrs['class'] = 'form-control'
        self.fields['product_name'].widget.attrs['type'] = 'text'

        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['type'] = 'text'
        self.fields['description'].widget.attrs['rows'] = 3

        self.fields['price'].widget.attrs['placeholder'] = 'Price'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['type'] = 'int'

        self.fields['stock'].widget.attrs['placeholder'] = 'Stock'
        self.fields['stock'].widget.attrs['class'] = 'form-control'
        self.fields['stock'].widget.attrs['type'] = 'int'

        self.fields['is_available'].widget.attrs['placeholder'] = 'Is available'
        self.fields['is_available'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_available'].widget.attrs['type'] = 'checkbox'


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']

    def __init__(self,*args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)

        self.fields['status'].widget.attrs['type'] = 'dropdown'
        self.fields['status'].widget.attrs['class'] = 'form-control'


       