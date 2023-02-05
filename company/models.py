from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User


class Tag(models.Model):
    """博客分类"""
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s' % (self.tag_name)


class Company(models.Model):
    name = models.CharField(verbose_name="企业名称", max_length=50)
    address = models.CharField(max_length=200, verbose_name="所在地")
    logo = models.ImageField(upload_to='company', verbose_name="LOGO", null=False)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="关联用户")
    introduce = models.TextField(verbose_name="企业简介", max_length=400)
    phone = models.CharField(blank=True, help_text='联系电话', max_length=20)
    created_date = models.DateTimeField(verbose_name="注册日期", auto_now=True)
    modified_date = models.DateTimeField(verbose_name="注册日期", auto_now_add=True)

    class Meta:
        verbose_name = _('企业')
        verbose_name_plural = _('企业列表')
        ordering = ['-created_date']

    def __str__(self):
        return self.name

    def get_user(self):
        return self.user

    def get_url(self):
        return reverse('company_detail', kwargs={'company_pk': self.pk})
