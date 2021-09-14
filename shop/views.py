from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView                      
from .models import (                     
    Product,
    Category
)
app_name = 'shop'

class HomeView(ListView):
    model = Product
    queryset = Product.objects.order_by('-created_on')
    template_name = "store.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product.html"
    
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
    
class SpectroscopyListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='spectroscopy')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/analytical.html'
    
class TestMeasurementListView(ListView):
    model= Product
    category_id = Category.objects.filter(slug='test-measurement')
    queryset = Product.objects.filter(
        category__in=category_id).order_by('-created_on')
    template_name = 'store/testmeasurement.html'
