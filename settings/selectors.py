from settings.models import Setting


def get_global_settings():
    return Setting.get_solo()
