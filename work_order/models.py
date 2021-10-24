from django.db import models
from property.models import Apartment
from user.models import AppUser

# Create your models here.
class WorkOrder(models.Model):
    description = models.CharField(max_length=200, blank=False, default='')
    skillset_required = models.CharField(max_length=200, blank=False, default='')
    severity_level = models.CharField(max_length=20, blank=False, default='')
    current_status = models.CharField(max_length=25, blank=False, default='')
    desired_completion_date = models.DateTimeField(blank=True)
    actual_completion_date = models.DateTimeField(blank=True)
    estimated_cost = models.DecimalField(max_digits=8, decimal_places=2, default='0.0')
    actual_cost = models.DecimalField(max_digits=8, decimal_places=2, default='0.0')
    apartment_id = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    user_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)

class WorkOrderItem(models.Model):
    item_name = models.CharField(max_length=30, blank=False)
    item_cost = models.DecimalField(max_digits=8, decimal_places=2, default='0.0')
    work_order_id= models.ForeignKey(WorkOrder, on_delete=models.CASCADE)