# _*_coding:utf-8_*_
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    '''
    # 文章分类的名字，继承了model.Model类
    '''
    name = models.CharField(max_length=100)
    # name为models.CharField的实例
class Tag(models.Model):
    '''
    文章的标签，继承models.Model类
    '''
    name = models.CharField(max_length=100)
    
class Post(models.Model):
    '''
    文章的数据库表格
    '''
    title = models.CharField(max_length=70)
    # 文章正文，我们使用了 TextField。
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    
    excerpt = models.CharField(max_length=200, blank=True)
    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # ForeignKey，即一对多的关联关系。
    # 建外键时，ForeignKey包含两个参数.当一个model对象的ForeignKey关联的对象被删除时，默认情况下此对象也会一起被级联删除的。
    tags = models.ManyToManyField(Tag, blank=True)
    # ManyToManyField，表明这是多对多的关联关系。
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #这里 User 是从 django.contrib.auth.models 导入的
    #一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系