# barbershop_app/views.py
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.http import JsonResponse
from .models import Master, Service, Appointment
from .forms import AppointmentForm


class IndexView(TemplateView):
    template_name = 'index.html'


class MastersView(TemplateView):
    template_name = 'masters.html'


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointment_form.html'
    success_url = '/thank-you/'


class ThankYouView(TemplateView):
    template_name = 'thank_you.html'


class OurContactView(TemplateView):
    template_name = 'our_contact.html'


def load_services(request):
    master_id = request.GET.get('master_id')
    print(f"Received master_id: {master_id}") # Лог получения master_id
    services = Service.objects.filter(master_id=master_id).values('id', 'name')
    services_list = list(services)
    print(f"Returning services: {services_list}") # Лог возвращаемых услуг
    return JsonResponse({'services': services_list})

# def load_services(request):
#     master_id = request.GET.get('master_id')
#     services = Service.objects.filter(masters__id=master_id).order_by('name')
#     return JsonResponse(list(services.values('id', 'name')), safe=False)
