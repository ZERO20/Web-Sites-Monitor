from django.contrib import admin

from Apps.Monitor.models import Configuration, Monitoring


# Register your models here.

@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    pass


@admin.register(Monitoring)
class MonitoringAdmin(admin.ModelAdmin):
    pass