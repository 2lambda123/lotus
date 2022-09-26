from django.contrib import admin
from rest_framework_api_key.admin import APIKeyModelAdmin
from rest_framework_api_key.models import APIKey
from django.contrib.auth.admin import UserAdmin

from .models import (
    APIToken,
    BillableMetric,
    BillingPlan,
    Customer,
    Event,
    Invoice,
    Organization,
    PlanComponent,
    Subscription,
    User,
    Alert,
)

# Register your models here.
admin.site.register(Customer)
admin.site.register(Alert)
admin.site.register(Event)
admin.site.register(BillingPlan)
admin.site.register(Subscription)
admin.site.register(Invoice)
admin.site.register(BillableMetric)
admin.site.register(PlanComponent)
admin.site.register(User, UserAdmin)
admin.site.register(Organization)

admin.site.unregister(APIKey)


@admin.register(APIToken)
class UserAPIKeyModelAdmin(APIKeyModelAdmin):
    pass