from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from eshopapi.models import User, Shop
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


# Register your models here.
# Теперь необходимо подключить нашу пользовательскую модель к админке

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""
    # Расширяем исходный класс UserAdmin, предоставляемый администратором Django
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_admin')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(Shop)
