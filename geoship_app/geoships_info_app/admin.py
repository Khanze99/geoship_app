from django.contrib import admin
from .models import Vessel, History


class HistoryInLine(admin.TabularInline):
    model = History


class VesselAdm(admin.ModelAdmin):
    inlines = [
        HistoryInLine,
    ]


admin.site.register(Vessel, VesselAdm)
admin.site.register(History)
