from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(CustomLogin)
admin.site.register(Register)
admin.site.register(Deposits)
admin.site.register(LoanApplication)