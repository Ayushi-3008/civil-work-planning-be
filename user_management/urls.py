from django.urls import path
from user_management.views import (DepartmentView)

urlpatterns = [
    path('department/', DepartmentView.as_view(), name='department')
]


