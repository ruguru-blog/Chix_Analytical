from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import (
    HomeView,
    ProductDetailView, AnalyticalListView,
    ChromatographyListView,ClinicalListView,LaboratoryListView,
    MedicalListView,MicroscopesListView,
    ProcessListView,SemiConductorListView,
    SpectroscopyListView,TestMeasurementListView
)

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ProductDetailView.as_view(), name ="product"),
    path("analytical/", AnalyticalListView.as_view(), name="analytical"),
    path('chromatography/',ChromatographyListView.as_view(), name="chromatography"),
    path('clinical/',ClinicalListView.as_view(), name="clinical"),
    path('laboratory/',LaboratoryListView.as_view(), name="laboratory"),
    path('medical/',MedicalListView .as_view(), name="medical"),
    path('microscopes/',MicroscopesListView.as_view(), name="microscopes"),
    path('process/',ProcessListView.as_view(), name="process"),
    path('spectroscopy/',SpectroscopyListView.as_view(), name="spectroscopy"),
    path('semiconductor/',SemiConductorListView.as_view(), name="semiconductor"),
    path('testmeasurement/',TestMeasurementListView.as_view(), name="testmeasurement"),







    

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

