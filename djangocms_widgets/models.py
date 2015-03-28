# coding: utf-8

"""
    djangocms-widgets
    ~~~~~~~~~~~~~~~~~

    :copyleft: 2015 by the djangocms-widgets team, see AUTHORS for more details.
    :created: by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from cms.utils.compat.dj import python_2_unicode_compatible
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from cms.utils.helpers import reversion_register


TEMPLATE_CHOICES = [(x, _(y)) for x, y in settings.WIDGET_TEMPLATES]

@python_2_unicode_compatible
class Widget(CMSPlugin):
    template = models.CharField(_("template"), max_length=100, choices=TEMPLATE_CHOICES,
        help_text=_('The template used to render this widget.')
    )

    class Meta:
        ordering = ['template']
        verbose_name = _("Widget")
        verbose_name_plural = _("Widgets")

    def __str__(self):
        return self.template

reversion_register(Widget)
