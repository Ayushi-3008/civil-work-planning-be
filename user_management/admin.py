from django.contrib import admin
from .models import (Department, SubDepartment, Role, User, Permission, PermissionTemplate, Dashboard)

# Register your models here.
admin.site.register(Department)
admin.site.register(SubDepartment)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(PermissionTemplate)
admin.site.register(Permission)
admin.site.register(Dashboard)