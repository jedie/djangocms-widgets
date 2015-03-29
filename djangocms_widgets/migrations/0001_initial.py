# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, to='cms.CMSPlugin', serialize=False, primary_key=True)),
                ('template', models.CharField(max_length=100, choices=[('socialshareprivacy.html', 'SocialSharePrivacy'), ('widget/dawanda.html', 'DaWanda')], help_text='The template used to render this widget.', verbose_name='template')),
            ],
            options={
                'verbose_name_plural': 'Widgets',
                'ordering': ['template'],
                'verbose_name': 'Widget',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
