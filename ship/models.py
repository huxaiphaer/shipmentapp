import uuid as uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django_extensions.db.models import TimeStampedModel

from user.models import User

STATUSES = [
    ('AD', 'Arrived'),
    ('PD', 'Pending'),
    ('OTW', 'On the way'),
    ('FD', 'Failed'),
]

PENDING = 'Pending'


class Shipment(TimeStampedModel, models.Model):
    """
    Shipment model.
    """
    uuid = models.UUIDField(unique=True, max_length=500,
                            default=uuid.uuid4,
                            editable=False,
                            db_index=True, blank=False, null=False)
    package_name = models.CharField(_('Package Name'), max_length=255,
                                    blank=True, null=True)
    shipping_date = models.DateField(_('Shipping Date'), null=True)
    arrival_date = models.DateField(_('Arrival Date'), null=True)
    status = models.CharField(
        _('Status'),
        max_length=100,
        choices=STATUSES,
        default=PENDING,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='shipment_user')
    country_of_origin = CountryField()
    destination_country = CountryField()

    def __str__(self):
        return self.package_name

    class Meta:
        verbose_name_plural = "Shipment"
        ordering = ['-created', ]

