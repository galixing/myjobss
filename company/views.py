from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType

from comment.forms import CommentForm
from .forms import CompanyForm
from .models import Company
from jobs.models import Job
from comment.models import Comment


# Create your views here.
def companies_list(request):
    company_list = Company.objects.all()
    return render(request, 'company/list.html', locals())


def detail(request, company_pk):
    company = get_object_or_404(Company, pk=company_pk)
    jobs = Job.objects.filter(creator=company.user)
    company_content_type = ContentType.objects.get_for_model(company)
    comment_form = CommentForm(initial={'content_type': company_content_type.model, 'object_id': company_pk,'reply_comment_id':0})
    comments = Comment.objects.filter(content_type=company_content_type, object_id=company.pk, parent=None)
    response = render(request, 'company/detail.html', locals())  # 响应
    return response


def add(request):
    if request.method == 'GET':
        form = CompanyForm()
        return render(request, 'company/add.html', locals())
    else:
        name = request.POST.get('name')
        address = request.POST.get('address')
        logo = request.POST.get('logo')
        user = request.user
        introduce = request.POST.get('introduce')
        phone = request.POST.get('phone')

        c = Company()
        c.name = name
        c.address = address
        c.logo = logo
        c.user = user
        c.introduce = introduce
        c.save()

        return render(request, 'index.html', locals())
