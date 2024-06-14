# # barbershop_app/admin.py
# from django.contrib import admin
# from .models import Master, Service, Appointment
#
#
# @admin.register(Master)
# class MasterAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name', 'phone', 'gender')
#     search_fields = ('first_name', 'last_name', 'phone')
#     list_filter = ('gender',)
#
#
# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price')
#     search_fields = ('name',)
#     list_filter = ('price',)
#
#
# @admin.register(Appointment)
# class AppointmentAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'phone', 'master', 'service', 'created_at', 'status')
#     search_fields = ('first_name', 'phone', 'master__first_name', 'master__last_name', 'service__name')
#     list_filter = ('status', 'created_at')
