from django.contrib import admin

# Register your models here.
from jobs.models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    fields = [ 'name', 'job_city', 'job_type', 'job_responsibility', 'job_requirement', 'creator', 'created_date',
    'modified_date']
    list_display = (
    'id', 'name', 'job_city', 'job_type', 'job_responsibility', 'job_requirement', 'creator', 'created_date',
    'modified_date')
