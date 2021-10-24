from django.contrib import admin

# Register your models here.
from work_order.models import WorkOrder, WorkOrderItem

admin.site.register(WorkOrder)
admin.site.register(WorkOrderItem)
