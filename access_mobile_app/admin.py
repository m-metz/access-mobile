from django.contrib import admin
from .models import DonorAccount, DoneeAccount, Sponsorship

class DonorAccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'is_active', 'is_staff', 'date_joined')

admin.site.register(DonorAccount, DonorAccountAdmin)
admin.site.register(DoneeAccount)
admin.site.register(Sponsorship)