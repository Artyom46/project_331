from django.db import models


class Master(models.Model):
    """
    Модель Мастера. Содержит данные о работающих мастерах.
    """
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    avatar = models.ImageField(upload_to='media/barbers/avatars/')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Service(models.Model):
    """
    Модель Услуги. Содержит название услуги, цену услуги. Мастера - услуги - многие ко многим.
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    masters = models.ManyToManyField(Master, related_name='services')

    def __str__(self):
        return self.name


class Appointment(models.Model):
    """
    Модель Запись. Служит для записи к мастеру, на выбранные услуги, без указания времени.
    """
    STATUS_CHOICES = [
        ('P', 'Processed'),
        ('U', 'Unprocessed'),
    ]

    first_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    comments = models.TextField(blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='U')

    def __str__(self):
        return f'Запись: {self.first_name} к {self.master.first_name}'
