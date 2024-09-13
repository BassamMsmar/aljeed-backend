from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.db import models 

# Create your models here.
class Company(models.Model):
    name = models.CharField(_("Company Name"), max_length=100)
    logo = models.ImageField(_("Company Logo"), upload_to='company')
    cover = models.ImageField(_("Company Cover"), upload_to='company', null=True, blank=True)
    subtitle = models.TextField(_("Subtitle"), max_length=500)
    facebool_link = models.URLField(_("Facebool_link"), max_length=200, null=True, blank=True)
    twitter_link = models.URLField(_("Twitter_link"), max_length=200, null=True, blank=True)
    youtube_link = models.URLField(_("Youtube_link"), max_length=200, null=True, blank=True)
    phone = models.IntegerField(_("Company Phone"), null=True, blank=True)
    email = models.EmailField(_("Company Email"), max_length=500, null=True, blank=True)
    address = models.TextField(_("Company Address"), max_length=500, null=True, blank=True)
    android_app = models.URLField(_("Android app"), max_length=200, null=True, blank=True)
    ios_app = models.URLField(_("ios app"), max_length=200, null=True, blank=True)
    call_us = models.IntegerField(_("call us"), null=True, blank=True)
    email_us = models.EmailField(_("email us"), max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name