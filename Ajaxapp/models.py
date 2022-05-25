from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(unique=True,max_length=50)
    passwd=models.CharField(max_length=20)
    phone=models.BigIntegerField(unique=True)

    class Meta:
        db_table='student'