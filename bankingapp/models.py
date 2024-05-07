from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomLogin(AbstractUser):
    userType = models.CharField(max_length = 100)
    viewPass = models.CharField(max_length = 100)
    
class Register(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField()
    accountNum = models.IntegerField()
    accountType = models.CharField(max_length = 100)
    credit = models.IntegerField()
    balance = models.IntegerField(null=True)
    login_id = models.ForeignKey(CustomLogin,on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    
class Deposits(models.Model):
    user_id = models.ForeignKey(CustomLogin,on_delete = models.CASCADE)
    account = models.ForeignKey(Register,on_delete = models.CASCADE)
    amount = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(auto_now_add = True)
    message = models.CharField(max_length = 1000, null=True)

    def __str__(self):
        return self.account.name
    
class LoanApplication(models.Model):
    loan_amount = models.IntegerField()
    annual_income = models.IntegerField()
    loan_type = models.CharField(max_length = 100)
    name = models.CharField(max_length = 300)
    dob = models.DateField()
    marital_status = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.IntegerField()
    address = models.CharField(max_length = 2000)
    address_year = models.CharField(max_length = 100)
    employer = models.CharField(max_length=200)
    occupation = models.CharField(max_length = 100)
    experience = models.CharField(max_length = 100)
    income = models.IntegerField()
    mortgage = models.IntegerField()
    comments = models.CharField(max_length = 3000,null=True)
    bank = models.CharField(max_length = 2000)
    accountNum = models.IntegerField()
    aadhar = models.FileField(null = True)
    pan = models.FileField(null = True)
    register_id = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    login_id = models.ForeignKey(CustomLogin,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.name
    
class Complaints(models.Model):
    complaint = models.CharField(max_length = 2000)
    complaint_reply = models.CharField(max_length = 2000,null = True)
    user_id = models.ForeignKey(Register,on_delete = models.CASCADE,null = True)
    dateTime = models.DateTimeField(auto_now_add = True,null = True)
    login_id = models.ForeignKey(CustomLogin,on_delete = models.CASCADE)

    def __str__(self):
        return self.login_id.email 
