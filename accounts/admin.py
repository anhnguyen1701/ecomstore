from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account

# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username', 'first_name', 'last_name')   # link to detail page
    readonly_fields = ('last_login', 'date_joined') # read only
    ordering = ('-date_joined',) # sort in reverse 

    # required to declare
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)