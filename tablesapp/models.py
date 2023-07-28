from django.db import models
from django.utils.translation import gettext as _


class modelValues(models.Model):
    id = models.IntegerField(primary_key=True)
    landmark = models.CharField(
        _("Landmark"), max_length=255)
    turkish_male = models.CharField(
        _("Turkish Male"), max_length=255, null=True)
    turkish_female = models.CharField(
        _("Turkish Female"), max_length=255, null=True)
    caucasian_male = models.CharField(
        _("Caucasian Male"), max_length=255, null=True)
    caucasian_female = models.CharField(
        _("Caucasin Female"), max_length=255, null=True)
    korean_male = models.CharField(
        _("Korean Male"), max_length=255, null=True)
    korean_female = models.CharField(
        _("Korean Female"), max_length=255, null=True)
    brazillian_male = models.CharField(
        _("Brazil Male"), max_length=255, null=True)
    brazillian_female = models.CharField(
        _("Brazil Female"), max_length=255, null=True)
    indian_male = models.CharField(
        _("Indian Male"), max_length=255, null=True)
    indian_female = models.CharField(
        _("Indian Female"), max_length=255, null=True)
    german_male = models.CharField(
        _("Indian Male"), max_length=255, null=True)
    german_female = models.CharField(
        _("Indian Female"), max_length=255, null=True)
    srilankan_male = models.CharField(
        _("Indian Male"), max_length=255, null=True)
    srilankan_female = models.CharField(
        _("Indian Female"), max_length=255, null=True)
    taiwanese_male = models.CharField(
        _("Indian Male"), max_length=255, null=True)
    taiwanese_female = models.CharField(
        _("Indian Female"), max_length=255, null=True)

    def __str__(self):
        return str(self.id)
