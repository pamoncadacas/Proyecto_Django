# motos_api/admin.py
from django.contrib import admin
from .models import Moto

# Register your models here.
class MotoAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "trademark",
        "model",
        "price",
        "image",
        "supplier",
    )

admin.site.register(Moto, MotoAdmin)