from django.apps import AppConfig
import threading

class ApointementConfig(AppConfig):
    name = 'k_bot.apointement'

    def ready(self):
        from . import telegram_utils
        threading.Thread(target=telegram_utils.create_bot, daemon=True).start()