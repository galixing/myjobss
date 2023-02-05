from django import forms
from django.shortcuts import render

from resume.form import ResumeForm
from resume.models import Resume


def resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            re = Resume()
            re.name = request.POST.get('name')
            re.applicant = request.user
            re.city = request.POST.get('city')
            re.phone = request.POST.get('phone')
            re.email = request.POST.get('email')
            re.apply_position = request.POST.get('apply_position')
            re.born_address = request.POST.get('born_address')
            re.gender = request.POST.get('gender')
            re.picture = request.POST.get('picture')
            re.attachment = request.POST.get('attachment')
            re.bachelor_school = request.POST.get('bachelor_school')
            re.master_school = request.POST.get('master_school')
            re.doctor_school = request.POST.get('doctor_school')
            re.major = request.POST.get('major')
            re.degree = request.POST.get('degree')
            re.candidate_introduction = request.POST.get('candidate_introduction')
            re.work_experience = request.POST.get('work_experience')
            re.project_experience = request.POST.get('project_experience')
            re.save()
            return render(request, 'index.html', locals())
        else:
            raise forms.ValidationError('出错')

    else:
        form = ResumeForm()
        return render(request, 'resume/add_resume.html', locals())


def resume_list(request):
    list = Resume.objects.all()
    return render(request, 'resume/resume_list.html', locals())


def resume_detail(request, resume_pk):
    resume = Resume.objects.filter(pk=resume_pk)
    return render(request, 'resume_detail.html', locals())
