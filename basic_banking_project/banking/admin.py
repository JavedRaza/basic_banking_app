from django.contrib import admin

# Register your models here.
from .models import Customers , Transfer
admin.site.register(Customers)
admin.site.register(Transfer)
