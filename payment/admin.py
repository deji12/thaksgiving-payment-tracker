from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Payment

class PaymentAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = [
        'name',
        'matric_number',
        'amount',
        'part_time_student',
        'paid_when'
    ]

    list_filter = [
        'part_time_student',
        'is_part_payment',
        'paid_when',
        'amount'
    ]

    search_fields = [
        'name',
        'matric_number'
    ]

admin.site.register(Payment, PaymentAdmin)