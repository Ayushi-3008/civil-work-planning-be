from django.db import models
from django.db.models import Q, UniqueConstraint

# Create your models here.

class BaseModel (models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Department model
class Department(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'departments'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name
    
# Sub department model
class SubDepartment(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='sub_departments')

    class Meta:
        unique_together = ('name', 'department_id')
        db_table = 'sub_departments'
        verbose_name = 'Sub department'
        verbose_name_plural = 'Sub departments'

    def __str__(self):
        return self.name

# Role model
class Role(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'role'
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        return self.name

# Custom user model
class User (BaseModel):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    sub_department_id = models.ForeignKey(SubDepartment, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
    
# Dashboard model
class Dashboard(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    config = models.JSONField(blank=True, null=True)

    class Meta:
        db_table = 'dashboards'
        verbose_name = 'Dashboard'
        verbose_name_plural = 'Dashboards'

    def __str__(self):
        return self.name
    
# Custom permission_template model
class PermissionTemplate(BaseModel):
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name="permission_templates")
    action_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'permission_templates'
        verbose_name = 'Permission Template'
        verbose_name_plural = 'Permission Templates'
        unique_together = ('dashboard', 'action_name')  # prevent duplicate action for same dashboard

    def __str__(self):
        return f"{self.dashboard.name} - {self.action_name}"
  
# Custom permission model
class Permission(BaseModel):
    department_id = models.ForeignKey('Department', on_delete=models.CASCADE)
    sub_department_id = models.ForeignKey('SubDepartment', on_delete=models.CASCADE, null=True, blank=True)
    role_id = models.ForeignKey('Role', on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, null=True, blank=True)
    permission_template_id = models.ForeignKey('PermissionTemplate', on_delete=models.CASCADE)
    allowed = models.BooleanField(default=True)

    class Meta:
        db_table = 'permissions'
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'
        constraints = [
            # For Department-level permissions (no subdept, role, user)
            UniqueConstraint(
                fields=['department_id', 'permission_template_id'],
                condition=Q(sub_department_id__isnull=True, role_id__isnull=True, user_id__isnull=True),
                name='unique_dept_permission'
            ),
            # For SubDepartment-level permissions
            UniqueConstraint(
                fields=['department_id', 'sub_department_id', 'permission_template_id'],
                condition=Q(role_id__isnull=True, user_id__isnull=True),
                name='unique_subdept_permission'
            ),
            # For Role-level permissions
            UniqueConstraint(
                fields=['department_id', 'sub_department_id', 'role_id', 'permission_template_id'],
                condition=Q(user_id__isnull=True),
                name='unique_role_permission'
            ),
            # For User-level permissions
            UniqueConstraint(
                fields=['department_id', 'sub_department_id', 'role_id', 'user_id', 'permission_template_id'],
                name='unique_user_permission'
            ),
        ]

    def __str__(self):
        # Collect only non-null fields
        level_parts = [
            str(self.role_id) if self.role_id else None,
            str(self.user_id) if self.user_id else None,
            str(self.sub_department_id) if self.sub_department_id else None,
            str(self.department_id) if self.department_id else None,
        ]
        
        # Filter out None values and join with " / "
        level_info = " + ".join([p for p in level_parts if p])

        return (
            f"{self.permission_template_id.dashboard.name} - "
            f"{self.permission_template_id.action_name} → "
            f"{level_info} "
            f"(Allowed: {self.allowed})"
        )