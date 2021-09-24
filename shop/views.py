from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import ListView, DetailView                      
from .models import (Product,Category,Order,OrderItem)
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm, OrderCreateForm

app_name = 'shop'


# cart functionality
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)  # create a new cart object passing it the request object 
    product = get_object_or_404(Product, id=product_id) 
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'store/cart.html', {'cart': cart})

class HomeView(ListView):
    model = Product
    queryset = Product.objects.order_by('-created_on')
    template_name = "store.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product.html"
    
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'store/checkout.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'store/checkout.html', {'form': form})


class AnalyticalListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='analytical')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/analytical.html'

class ChromatographyListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='chromatography')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/chromatography.html'
    
    
class ClinicalListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='clinical')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/clinical.html'
    
    
class LaboratoryListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='laboratory')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/laboratory.html'
    
class MedicalListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='medical')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/medical.html'
    
class MicroscopesListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='microscopes')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/microscopes.html'
    
class ProcessListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='process')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/process.html'
    
class SemiConductorListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='semiconductor')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/semiconductor.html'
    
    
class TestMeasurementListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='test-measurement')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/testmeasurement.html'

class SpectroscopyListView(ListView):
    model = Product
    category_id = Category.objects.filter(slug='spectroscopy')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/spectroscopy.html'
