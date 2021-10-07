from django.shortcuts import render
from myguest.models import Guest
from django.http.response import HttpResponseRedirect

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    gdata = Guest.objects.all()
    #print(gdata)
    #print(Guest.objects.filter(id=1))
    #print(Guest.objects.filter(title__contains='방문'))  #밑줄 두개
    #print(Guest.objects.get(id=1))  #query set 이 아니라 단수로 출력됨
    
    #정렬 방법1
    #gdata = Guest.objects.all().order_by('title')  #asc
    #gdata = Guest.objects.all().order_by('-title')  #desc
    #gdata = Guest.objects.all().order_by('-id')     #desc
    #gdata = Guest.objects.all().order_by('-id')[0:2]
    #gdata = Guest.objects.all().order_by('-title', 'id') #1차키 2차키 3차키 ...
    #여기서 적용할 수도 있지만 models.py에서 적용할 수도 있다.
    
    return render(request, 'list.html', {'gdatas':gdata})

def InsertFunc(request):
    return render(request, 'insert.html')

from datetime import datetime

def InsertOkFunc(request):
    #print(request.POST.get('title'))
    #print(request.POST.get('content'))
    #print(request.POST['content'])
    
    #추가하기 insert SQL문 대신 ORM 메서드 사용
    if request.method == "POST":
        Guest(
            title = request.POST.get('title'),
            content = request.POST.get('content'),
            regdate = datetime.now()    
        ).save()
        
    #추가 후 목록보기
    return HttpResponseRedirect('/guest/')





