# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # email_password = .CharField(db_column='department_name', max_length=45)

    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = 'users'


class Department(models.Model):
    # id = models.PositiveSmallIntegerField(primary_key=True,editable=False)
    id = models.SmallAutoField(primary_key=True)
    department_name = models.CharField(db_column='department_name', max_length=45, unique=True)

    def __str__(self):
        return self.department_name

    class Meta:
        db_table = "department"


class Role(models.Model):
    id = models.SmallAutoField(primary_key=True,editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.role_name


    class Meta:
        db_table = "role"

