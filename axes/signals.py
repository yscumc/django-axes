from django.dispatch import receiver
from django.dispatch import Signal
from django.utils.timezone import now
from django.contrib.auth.signals import user_logged_out
from django.core.exceptions import ObjectDoesNotExist

from axes.models import AccessLog


user_locked_out = Signal(providing_args=['request', 'username', 'ip_address'])


@receiver(user_logged_out)
def log_user_lockout(sender, request, user, signal, *args, **kwargs):
    """ When a user logs out, update the access log
    """
    if not user:
        return

    try:
        username = user.get_username()
    except AttributeError:
        # Django < 1.5
        username = user.username

    try:
        session_key = request.session.session_key
    except AttributeError:
        session_key = None

    access_logs = AccessLog.objects.filter(
        # Don't filter by username because it can be changed during an open session
        # username=username,
        logout_time__isnull=True,
        session_id=session_key,
    ).order_by('-attempt_time')

    # There can be more than one AccessLog record if the user logged in
    # more than once in the same session
    access_logs.update(logout_time=now())
