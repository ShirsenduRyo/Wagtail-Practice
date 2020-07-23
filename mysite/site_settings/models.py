from django.db import models

# Create your models here.

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting
class SocialMediaSettings(BaseSetting):
    """ Social Media Settings"""
    facebook = models.URLField(blank = True, null = True, help_text = "Facebook Account")
    twitter = models.URLField(blank = True, null = True, help_text = "Twitter Account")
    youtube = models.URLField(blank = True, null = True, help_text = "Youtube Channel")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube")

        ])
    ]