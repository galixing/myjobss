from django import forms
from .models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['job_type','name','job_city','job_responsibility','job_requirement']
