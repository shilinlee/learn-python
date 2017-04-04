# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

#应用名字+Models
class DyModels(models.Model):
    #创建数据库 写入 读取
    id = models.AutoField(primary_key=True) #自动增长 增加主键
    title = models.CharField(max_length=100,null=False)
    content = models.TextField(null=False)
    link = models.CharField(max_length=100,null=False)


