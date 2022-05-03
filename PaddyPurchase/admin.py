from django.contrib import admin
from .models import PaddyPurchase
from import_export.admin import ExportActionMixin


# Register your models here.

class PaddyPurchaseAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = ['ref_no',
                    'token_no',
                    'date',
                    'agent_name',
                    'vehicle_no',
                    'farmer_name',
                    'farmer_address',
                    'agent_commission',
                    'net_total'
                    ]


admin.site.register(PaddyPurchase, PaddyPurchaseAdmin)
