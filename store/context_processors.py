from .models import Category, Sub_Category


def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)


def menu_sub_links(request):
    sub_links = Sub_Category.objects.all()
    return dict(sub_links=sub_links)
