from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate
from django.contrib import auth  # user model
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from area.models import Area
from comment.models import Comment
from company.models import Company
from jobs.models import Job
from resume.models import Resume


def index(request):
    sql = 'select company_company.* from company_company left join (select * from comment_comment where content_type_id = 8) as c on company_company.id = c.object_id group by company_company.id order by count(c.object_id) desc'

    companys = Company.objects.raw(sql)
    comments = Comment.objects.all().order_by('-comment_time')
    jobs = Job.objects.all().order_by('-created_date')
    company_list = Company.objects.all().order_by('-modified_date')

    return render(request, 'index.html', locals())


# 给rawqueryset对象加上len()方法
def add_len_to_raw_query(query):
    from django.db.models.query import RawQuerySet
    def __len__(self):
        from django.db import connection
        sql = 'select count(*) from (%s) as newsql' % query.raw_query
        with connection.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
        return row[0]

    setattr(RawQuerySet, '__len__', __len__)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。
        user = authenticate(request, username=username, password=password)
        # 验证如果用户不为空
        if user is not None:
            # login方法登录
            auth.login(request, user)
            # 返回登录成功信息
            return redirect(request.GET.get('from', reverse('index')))
        else:
            # 返回登录失败信息
            return HttpResponse('登陆失败')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        auth.login(request, user)
        referer = request.GET.get('from', reverse('index'))
        return redirect(referer)
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)
    # 记住来源的url，如果没有则设置为首页('/')
    returnPath = request.META.get('HTTP_REFERER', '/')
    # 重定向到原来的页面，相当于刷新
    return HttpResponseRedirect(returnPath)


def center(request, comments_user_pk):
    loginer = User.objects.filter(pk=comments_user_pk).first()
    company = Company.objects.filter(user=loginer)
    jobs = Job.objects.filter(creator=loginer)
    comments = Comment.objects.filter(user=loginer)
    return render(request, 'center.html', locals())


def myNotifications(request):
    return render(request, 'my_notifications.html', locals())


def search(request):
    search_words = request.GET.get('wd', '').strip()
    # 分词 & | ~
    condition = None
    for word in search_words.split(' '):
        if condition is None:
            condition = Q(name__icontains=word)
        else:
            condition = condition | Q(name__icontains=word)

    if condition is not None:
        search_of_company = Company.objects.filter(condition)
        search_of_jobs = Job.objects.filter(condition)
        search_of_resume = Resume.objects.filter(condition)

    return render(request, 'search.html', locals())


def test(request):
    return render(request, 'test.html')

class LoadAreaView(View):
    def get(self, request):
        # 获取请求参数
        pid = request.GET.get('pid', -1)
        pid = int(pid)

        # 根据父id查询区划信息
        areaList = Area.objects.filter(parentid=pid)

        # 进行序列化
        jareaList = serialize('json', areaList)

        return JsonResponse({'jareaList': jareaList})