
try:
    from offer.models import Range  # noqa
    OSCAR_INSTALLED = True
except ImportError:
    OSCAR_INSTALLED = False
