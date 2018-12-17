from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    role = models.CharField(max_length=40)
    created_at = models.DateTimeField('created at')

    def __str__(self):
        return self.role


class Department(models.Model):
    department = models.CharField(max_length=40)
    created_at = models.DateTimeField('created at')

    def __str__(self):
        return self.department


class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    contact = models.BigIntegerField(default=0)
    address = models.CharField(max_length=200)
    join_date = models.DateField('join_date')
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')

    def __str__(self):
        return str(self.user)


class Leave(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date_from = models.DateTimeField('from')
    date_to = models.DateTimeField('to')
    days = models.IntegerField(default=0)
    reason = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    approved_by = models.CharField(max_length=40)
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')

    def __str__(self):
        return self.id


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    assign_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    remarks = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    time_line = models.CharField(max_length=60,default='null')
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')

    def __str__(self):
        return self.project_name


class Task(models.Model):
    project = models.IntegerField()
    assign_by = models.IntegerField()
    assign_to = models.IntegerField()
    task = models.CharField(max_length=200)
    priority = models.CharField(max_length=40)
    remarks = models.CharField(max_length=200)
    status = models.CharField(max_length=40)
    assign_date = models.DateTimeField('assign_date')
    time_line = models.DateTimeField('time_line')
    created_at = models.DateTimeField('created at')
    updated_at = models.DateTimeField('updated at')

    def __str__(self):
        return self.project