
OSCAR_INSTALLED = False

try:
    from oscar.core.loading import get_model
    Range = get_model("offer", "range")
    if Range:
        OSCAR_INSTALLED = True
except ImportError:
    pass
