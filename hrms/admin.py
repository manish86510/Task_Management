from django.contrib import admin
from .models import Users, Department, Role, Leave, Project, Task

admin.site.register(Role)

admin.site.register(Department)

admin.site.register(Users)

admin.site.register(Leave)

admin.site.register(Project)

admin.site.register(Task)