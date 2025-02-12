from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView


from catalog.models import Product





class HomeListView(ListView):
    model = Product
    template_name = 'catalog/base.html'
    context_object_name = 'products'


# def home(request):
#     products = Product.objects.all()
#     context = {'products': products}
#     return render(request, 'base.html', context=context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        request.POST.get('message')
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')


def get(request):
    return render(request, 'catalog/contacts.html')


def post(request):

    name = request.POST.get('name')
    request.POST.get('message')
    return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")


class CatalogContactsView(View):
    pass


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


# def product_detail(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     context = {'product': product}
#     return render(request, 'product_detail.html', context=context)