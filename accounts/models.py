from oscar.core.loading import is_model_registered
from django.db import models
from accounts import abstract_models


if not is_model_registered('accounts', 'AccountType'):
    class AccountType(abstract_models.AccountType):
        pass


if not is_model_registered('accounts', 'Account'):
    class Account(abstract_models.Account):
        pass

    # Accounts are sometimes restricted to only work on a specific range of
    # products.  This is the only link with Oscar.
    from .utils import OSCAR_INSTALLED

    if OSCAR_INSTALLED:
        Account.add_to_class('product_range', models.ForeignKey(
            'offer.Range',
            null=True, blank=True))

if not is_model_registered('accounts', 'Transfer'):
    class Transfer(abstract_models.Transfer):
        pass


if not is_model_registered('accounts', 'Transaction'):
    class Transaction(abstract_models.Transaction):
        pass


if not is_model_registered('accounts', 'IPAddressRecord'):
    class IPAddressRecord(abstract_models.IPAddressRecord):
        pass
