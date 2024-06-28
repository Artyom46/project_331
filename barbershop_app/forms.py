# barbershop_app/forms.py
from django import forms
from .models import Appointment, Master, Service


class AppointmentForm(forms.ModelForm):
    """
    Форма для записи
    """
    class Meta:
        model = Appointment
        fields = ['master', 'first_name', 'phone', 'service', 'comments']
        widgets = {
            'master': forms.Select(attrs={'onchange': 'loadServices()', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'service': forms.Select(attrs={'onchange': 'loadServices()', 'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'cols': 1}),
        }

        labels = {
            'master': 'Выберите мастера',
            'first_name': 'Ваше имя',
            'phone': 'Номер телефона для обратной связи',
            'service': 'Выберите услугу',
            'comments': 'Комментарий/Пожелания',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.none()

        if 'master' in self.data:
            try:
                master_id = int(self.data.get('master'))
                self.fields['service'].queryset = Service.objects.filter(masters__id=master_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['service'].queryset = self.instance.master.services.order_by('name')
