from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User

# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)#规定了字段title属性为CharField()类型，并且以参数max_length=300的形式说明的最大数量
    author = models.ForeignKey(User, related_name="blog_posts")#通过字段atuhor规定了博客文章与用户之间的关系，一个用户对应多篇文章，ForeignKey()就反映了这种“一对多”的关系，类User就是BlogArticles的对应关系，related_name="blgo_posts"的作用是允许通过类User反向查询到BlogArticles
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:#貌似python中的元类，其实不是，在此处通过ordering=（“-publis”,）规定了BlogArticles实例对象的显示顺序，即按照publish字段值的倒序显示。
        ordering = ("-publish",)
    def __str__(self):
        return self.title