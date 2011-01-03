from django.contrib import admin
from aprspasscode.passcode.models import *

class PasscodeRequestAdmin(admin.ModelAdmin):
    readonly_fields = (
        'submitted',
        'passcode',
        'last_action',
        'action_by',
    )
    list_display  = (
        'full_name',
        'qrz',
        'qth',
        'email',
        'submitted',
        'decision',
        'status',
        'passcode',
        'last_action',
        'action_by',
    )
    list_filter = ('status',)
    search_fields = ['full_name', 'callsign', 'email',]
    actions = ['approve', 'deny']
    
    def approve(self, request, queryset):
        for passcode_request in queryset:
            passcode_request.approve()
    approve.short_description = "Approve all selected requests."
    
    def deny(self, request, queryset):
        for passcode_request in queryset:
            passcode_request.deny()
    deny.short_description = "Deny all selected requests."
    
    def save_model(self, request, obj, form, change):
        obj.action_by = request.user
        obj.save()

admin.site.register(PasscodeRequest, PasscodeRequestAdmin)