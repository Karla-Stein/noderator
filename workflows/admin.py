from django.contrib import admin
from .models import N8nConnection, GeneratedWorkflow

# Register your models here.
class N8nConnectionAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'is_verified',
    )

class GeneratedWorkflowAdmin(admin.ModelAdmin):
    list_display = (
        'workflow_id',
        'status',
        'created_at',
    )
    ordering = ('-created_at',)


admin.site.register(N8nConnection, N8nConnectionAdmin)
admin.site.register(GeneratedWorkflow, GeneratedWorkflowAdmin)