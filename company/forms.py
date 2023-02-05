from django.contrib.auth import forms
from django.forms import ModelForm

from company.models import Company


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ('created_date', 'modified_date','user')
