from django.contrib import admin

from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Subscriber
# Register your models here.

class SubscriberAdmin(ModelAdmin):
    """Subscriber Admin"""

    model = Subscriber

    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email","first_name","last_name")
    search_fields = ("email","first_name","last_name")
    
modeladmin_register(SubscriberAdmin)