# barbershop_app/urls.py
from django.urls import path
from . import views
from .views import IndexView, AppointmentCreateView, ThankYouView, MastersView, OurContactView, load_services

app_name = 'barbershop_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('appointment/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('thank-you/', ThankYouView.as_view(), name='thank_you'),
    path('load-services/', views.load_services, name='load_services'),
    path('masters/', MastersView.as_view(), name='masters'),
    path('our_contact/', OurContactView.as_view(), name='contact'),
]
