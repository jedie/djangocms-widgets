# coding: utf-8

"""
    djangocms-widgets
    ~~~~~~~~~~~~~~~~~

    :copyleft: 2015 by the djangocms-widgets team, see AUTHORS for more details.
    :created: by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from .models import Widget
from django.contrib import admin

class WidgetAdmin(admin.ModelAdmin):
    pass

admin.site.register(Widget, WidgetAdmin)
