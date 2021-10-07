from django.shortcuts import render
from myapp.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def showFunc(request):
    #SQL문을 객체로 만들어 두는 것 : ORM
    datas = Article.objects.all()  #select * from Article 이 수행됨
    #print(datas)  #<QuerySet [<Article: Article object (3)>, <Article: Article object (4)>]>
    #print(datas[0].name)  #마우스
    return render(request, 'list.html', {'articles':datas})  #QuerySet을 전달