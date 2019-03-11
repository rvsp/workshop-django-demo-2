from django.contrib import admin

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .models import UserDetails

# Register your models here.

class UserAdmin(BaseUserAdmin):
	add_form = UserCreationForm

	list_display = ('username','email','is_superuser')
	list_filter = ('is_superuser',)

	fieldsets = (
			(None, {'fields': ('username','email','password')}),
			('Permissions', {'fields': ('is_superuser',)})
		)
	search_fields = ('username','email')
	ordering = ('username','email')

	filter_horizontal = ()

admin.site.register(UserDetails, UserAdmin)

admin.site.unregister(Group)