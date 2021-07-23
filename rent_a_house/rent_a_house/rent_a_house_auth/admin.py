from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from rent_a_house.rent_a_house_auth.models import RentAHouseUser


@admin.register(RentAHouseUser)
class RentAHouseUserAdmin(UserAdmin):
    # list_display = ('email', 'first_name', 'last_name', 'is_staff')
    # list_filter = ('is_staff', 'is_superuser', 'groups')
    # search_fields = ('first_name', 'last_name', 'email')
    # ordering = ('email',)
    #
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'profile_image')}),
    #     ('Permissions', {
    #         'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
    #     }),
    #     ('Important dates', {'fields': ('last_login', 'date_joined')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # )
    #
    # readonly_fields = ('date_joined', )

    list_display = ('email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    readonly_fields = ('date_joined', )
