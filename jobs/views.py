from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from company.models import Company
from .form import JobForm
from .models import Job



@login_required
def add(request):
    if request.method == 'GET':
        form = JobForm()
        return render(request, 'jobs/add_job.html', locals())
    else:
        job_form = JobForm(request.POST)
        job = Job()
        if job_form.is_valid():
            job.name = job_form.cleaned_data['name']
            job.job_city = job_form.cleaned_data['job_city']
            job.job_type = job_form.cleaned_data['job_type']
            job.job_responsibility = job_form.cleaned_data['job_responsibility']
            job.job_requirement = job_form.cleaned_data['job_requirement']
            job.creator = request.user

            job.save()
            return render(request, 'index.html', locals())
        else:
            return render(request, 'index.html', locals())

def job_detail(request, job_pk):
    job = get_object_or_404(Job, pk=job_pk)
    jobs = Job.objects.all()
    #关联企业
    # user = request.user
    user = job.creator
    if user != AnonymousUser:
        company = get_object_or_404(Company,user=user)
    else:
        return render(request,'users/login.html')

    return render(request, 'jobs/detail.html', locals())


def joblist(request):
    job_list = Job.objects.all()
    paginator = Paginator(job_list, 6)
    page_num = request.GET.get('page', 1)
    page_of_job = paginator.get_page(page_num)
    current_page_num = page_of_job.number

    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    # 加上省略页码标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    return render(request, 'jobs/job_list.html', locals())
