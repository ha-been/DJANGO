from django.shortcuts import render
from mysangpum.models import Sangdata
from django.http.response import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')


def ListFunc(request):
    #SQL문 직접 작성도 가능하나 번거롭다.  html 에서 받을 때는 {{s.0}} s의 0번째 이런식으로 받아준다.
    #ORM은 깔끔하다.
    #datas = Sangdata.objects.all()
    #return render(request, 'list.html', {'sangpums':datas})

    #페이지 나누기
    datas = Sangdata.objects.all().order_by('-code')
    paginator = Paginator(datas, 3)  #페이지 당 3행씩 출력
    try:
        page = request.GET.get('page')
    except:
        page = 1
        
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1) #페이지가 정수가 아닌 경우 1페이지를 보여준다.
    except EmptyPage:
        data = paginator.page(paginator.num_pages()) #페이지가 받아들여지지 않은 경우
        
    #개별 페이지 표시
    allpage = range(paginator.num_pages +1)  #num_pages 전체페이지 수
    #print(allpage)
    
    return render(request, 'list2.html', {'sangpums':data, 'allpage':allpage}) #datasX dataO


def InsertFunc(request):
    return render(request, 'insert.html')


def InsertOkFunc(request):
    if request.method == 'POST':
        try:  #추가하려는 자료가 이미 있다면 추가 화면으로 돌아간다
            Sangdata.objects.get(code=request.POST.get('code'))
            return render(request, 'insert.html', {'msg':'이미 등록된 번호입니다.'})
        except:
            Sangdata(
                code = request.POST.get('code'),
                sang = request.POST.get('sang'),
                su = request.POST.get('su'),
                dan = request.POST.get('dan')
            ).save()
        
    return HttpResponseRedirect('/sangpum/list')  #클라이언트가 요청하여 list를 보도록 함 


def UpdateFunc(request):
    data = Sangdata.objects.get(code = request.GET.get('code'))
    return render(request, 'update.html', {'sang_one':data})


def UpdateOkFunc(request):
    if request.method == 'POST':
        upRec = Sangdata.objects.get(code=request.POST.get('code'))
        upRec.code = request.POST.get('code')
        upRec.sang = request.POST.get('sang')
        upRec.su = request.POST.get('su')
        upRec.dan = request.POST.get('dan')
        upRec.save()
    
    return HttpResponseRedirect('/sangpum/list')


def DeleteFunc(request):
    delRec = Sangdata.objects.get(code=request.GET.get('code'))
    delRec.delete()
    
    return HttpResponseRedirect('/sangpum/list')


