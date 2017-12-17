from django.shortcuts import render,get_object_or_404
from blog import models

# Create your views here.

def blog_title(request):#视图函数，其中request负责响应接收到的请求且不能少，并总位于第一的位置，除了这个不可获取的参数，还可以根据需要在其后增加别的参数。
    blogs = models.BlogArticles.objects.all()#利用objects.all()获取BlogArticles里的数据（通过数据库）
    return render(request, "blog/titles.html", {"blogs":blogs})#结束当前函数，并返回结果，render()的作用是将数据渲染到制定模板上，第一个参数必须是request，数据是通过字典的形式传输给模板的。


def blog_article(request, article_id):
    #article = models.BlogArticles.objects.get(id = article_id)
    article = get_object_or_404(models.BlogArticles,id = article_id)
    pub = article.publish
    return render(request, 'blog/content.html',{"article":article, 'publish':pub})

def index(request):
    return render(request, 'home.html')