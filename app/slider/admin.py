from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderItem


@admin.register(SliderItem)
class SliderItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('image', 'title')
