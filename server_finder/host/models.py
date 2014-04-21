"""
host models module
"""
#django modules
from django.db import models
from django.utils.translation import ugettext_lazy as _


class IPRange(models.Model):
    """ IP Range class """
    pass


class Host(models.Model):
    """ Host model class """
    name = models.CharField(
        max_length=255, null=False, blank=False,
        help_text=_("name"),
    )

    ip_address = models.GenericIPAddressField(
        null=True, blank=True,
        help_text=_("IP Address"),
    )

    fqdn = models.CharField(
        max_length=255, null=True, blank=True,
        help_text=_("FQDN"),
    )

    host_detected = models.BooleanField(
        null=False, blank=False, default=False,
        help_text=_("ホスト検知"),
    )

    last_detection_check_date = models.DateTimeField(
        auto_now=True, auto_now_add=True,
        help_text=_("最終ホスト検知チェック日時"),
    )

    last_detected_date = models.DateTimeField(
        auto_now=False, auto_how_add=True,
        help_text=_("最終ホスト検知日時"),
    )


class Note(models.Model):
    """ Note model class """
    host = models.ForeignKey(
        Host, null=False, blank=False,
        help_text=_("host"),
    )

    subject = models.CharField(
        mex_length=255, null=False, blank=False,
        help_text=_("subject"),
    )

    body = models.TextField(
        max_length=5000, null=False, blank=False,
        help_text=_("body"),
    )
