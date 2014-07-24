from django.conf import settings
from django.utils.importlib import import_module


def reset(ip=None, username=None):
    """Reset records that match ip or username, and
    return the count of removed attempts.
    """
    from axes.models import AccessAttempt
    count = 0

    attempts = AccessAttempt.objects.all()
    if ip:
        attempts = attempts.filter(ip_address=ip)
    if username:
        attempts = attempts.filter(username=username)

    if attempts:
        count = attempts.count()
        attempts.delete()

    return count


def get_session_model():
    get_session_model.session_model = getattr(get_session_model, 'session_model', None)
    if not get_session_model.session_model:
        session_eng = import_module(settings.SESSION_ENGINE)
        # Assume the model is named Session, raise AttributeError if otherwise
        get_session_model.session_model = getattr(session_eng, 'Session')
    return get_session_model.session_model
