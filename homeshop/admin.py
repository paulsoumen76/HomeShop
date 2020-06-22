from django.contrib import admin
from homeshop.models import MobileTable,OrderTable,OrderUpdate,ContactDetails
# Register your models here.
admin.site.register(MobileTable)
admin.site.register(OrderTable)
admin.site.register(OrderUpdate)
admin.site.register(ContactDetails)
