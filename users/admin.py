from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Department, Role


'''
add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)



list_display = ['name','address','city','state','list_of_amenities']
    def list_of_amenities(self, obj):
        return ("%s" % ','.join([amenity.name for amenity in obj.amenities.all()]))
    list_of_amenities.short_description = 'Store amenities'

admin.site.register(Store, StoreAdmin)





'''

class RoleInline(admin.TabularInline):
    # this model has forgin key on users
    model = Role
    extra = 1
    max_num =1
    fields = ('department', 'role_name')

class DepartmentInline(admin.StackedInline):
    model = Department


class RoleAdmin(admin.ModelAdmin):

    list_display = ('department', 'role_name','user')
    list_filter = ('department','role_name',)
    # def view_role(self, obj):
    #     return obj.role_name

    # view_role.empty_value_display = '???'

class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('department', 'role_name','user')

    # def view_role(self, obj):
    #     return obj.role_name

    # view_role.empty_value_display = '???'


class CustomUserAdmin(UserAdmin):
    date_hierarchy = 'date_joined'
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff','view_role')
    model = CustomUser
    inlines = [
        RoleInline,
    ]

    def view_role(self, obj):
        return Role.objects.get(id=obj.id)
    view_role.short_description = 'Role Assign'
    view_role.empty_value_display = 'No Role'


admin.site.register(Department)
# admin.site.register(AdminProduction)
admin.site.register(Role, RoleAdmin)




admin.site.register(CustomUser, CustomUserAdmin)


