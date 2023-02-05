from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name','address','phone','user',)
    fields = ['user','name','introduce','address','phone']