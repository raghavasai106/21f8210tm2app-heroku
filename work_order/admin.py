from django.contrib import admin
from .models import WorkOrder, WorkOrderItem


class WorkOrderAdmin(admin.ModelAdmin):
   model = WorkOrder
   list_display = ['work_order_name', 'apartment_id', 'description', 'skillset_required', 'severity_level', 'current_status', 'desired_completion_date', 'actual_completion_date', 'estimated_cost', 'actual_cost', 'work_order_date', 'user_id']
   list_filter = ['apartment_id', 'skillset_required', 'severity_level', 'current_status', 'estimated_cost', 'actual_cost', 'work_order_date', 'actual_completion_date', 'user_id']
   fieldset = (
         ('Work Order Information', {
            'fields': ('work_order_name', 'apartment_id', 'description', 'skillset_required', 'severity_level', 'current_status', 'desired_completion_date', 'actual_completion_date', 'estimated_cost', 'actual_cost', 'work_order_date', 'user_id')
        })
   )
   add_fieldset = (
         ('Work Order Information', {
            'fields': ('work_order_name', 'apartment_id', 'description', 'skillset_required', 'severity_level', 'current_status', 'desired_completion_date', 'actual_completion_date', 'estimated_cost', 'actual_cost', 'work_order_date', 'user_id')
        })
   )
class WorkOrderItemAdmin(admin.ModelAdmin):
   model = WorkOrderItem
   list_display = ['item_name', 'item_cost', 'item_quantity', 'work_order_id']
   fieldset = (
         ('Work Order Item Information', {
            'fields': ('item_name', 'item_cost', 'item_quantity', 'work_order_id')
        })
   )
   add_fieldset = (
         ('Work Order Item Information', {
            'fields': ('item_name', 'item_cost', 'item_quantity', 'work_order_id')
        })
   )

admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(WorkOrderItem, WorkOrderItemAdmin)
