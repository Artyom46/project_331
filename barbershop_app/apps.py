from django.apps import AppConfig


class BarbershopAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'barbershop_app'

    def ready(self):
        """
        Ready - это метод, который вызывается при загрузке приложения.
        Мы можем здесь подписываться на сигналы.
        """
        import barbershop_app.signals
