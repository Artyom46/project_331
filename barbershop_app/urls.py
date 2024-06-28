# barbershop_app/urls.py
from django.urls import path
from . import views
from .views import IndexView, AppointmentCreateView, ThankYouView, MastersView, OurContactView, load_services

app_name = 'barbershop_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Главная страница
    path('appointment/', AppointmentCreateView.as_view(), name='appointment_create'),  # Форма для записи
    path('thank-you/', ThankYouView.as_view(), name='thank_you'),  # Страница с благодарностью за запись
    path('load-services/', views.load_services, name='load_services'),  # Выбор мастера и услуги
    path('masters/', MastersView.as_view(), name='masters'),  # Страница с мастерами
    path('our_contact/', OurContactView.as_view(), name='contact'),  # Страница с контактами
]
