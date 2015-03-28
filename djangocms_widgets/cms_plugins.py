# coding: utf-8

"""
    djangocms-widgets
    ~~~~~~~~~~~~~~~~~

    :copyleft: 2015 by the djangocms-widgets team, see AUTHORS for more details.
    :created: by JensDiemer.de
    :license: GNU GPL v3 or above, see LICENSE for more details.
"""

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool


from .models import Widget

class WidgetPlugin(CMSPluginBase):
    model = Widget
    name = _("Widget")
    text_enabled = True

    def get_render_template(self, context, instance, placeholder):
        return instance.template

    def icon_src(self, instance):
        return settings.STATIC_URL + "cms/img/icons/plugins/snippet.png"

plugin_pool.register_plugin(WidgetPlugin)
