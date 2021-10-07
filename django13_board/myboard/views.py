from django.shortcuts import render
from myboard.models import BoardTab
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from django.http.response import HttpResponseRedirect

# Create your views here.
def MainFunc(request):
    aa = "<div><h1>메인화면</h1></div>"
    return render(request, 'main.html', {'main':aa})


def ListFunc(request):
    #datas = BoardTab.objects.all().order_by('-id')
    datas = BoardTab.objects.all().order_by('-gnum','onum')  #댓글이 있는 경우 #그룹번호는 desc, 댓글은 asc
    paginator = Paginator(datas, 5)  #한 화면에 5행씩 출력
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
        
    return render(request, 'board.html', {'data':data})


def InsertFunc(request):  
    return render(request, 'insert.html')


def InsertOkFunc(request):  #새글 등록
    if request.method == "POST":
        try:  
            #그룹번호 구하기
            gbun = 1
            datas = BoardTab.objects.all()
            if datas.count() != 0:
                gbun = BoardTab.objects.latest('id').id + 1

            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = request.META['REMOTE_ADDR'],
                bdate = datetime.now(),
                readcnt = 0,  #초기값 0
                gnum = gbun,
                onum = 0,
                nested = 0
                
            ).save()
        
        except Exception as e:
            print('추가오류: ', e)
            
    return HttpResponseRedirect('/board/list')  #추가 후 목록보기


def ContentFunc(request):
    data = BoardTab.objects.get(id=request.GET.get('id'))
    data.readcnt += 1 # 조회수 증가
    data.save() #수정
    page = request.GET.get('page')
    
    return render(request, 'content.html', {'data_one':data, 'page':page})


def UpdateFunc(request):
    try:
        data = BoardTab.objects.get(id = request.GET.get('id'))
        
    except Exception as e:
        print('UpdateFunc err: ', e)
    
    return render(request, 'update.html', {'data_one':data})


def UpdateOkFunc(request):
    upRec = BoardTab.objects.get(id = request.POST.get('id'))
    print(upRec.passwd)
    print(request.POST.get('up_passwd'))
    
    if upRec.passwd == request.POST.get('up_passwd'):  #비밀번호가 일치하면 수정
        upRec.name = request.POST.get('name')
        upRec.mail = request.POST.get('mail')
        upRec.title = request.POST.get('title')
        upRec.cont = request.POST.get('cont')
        upRec.save()

    else:
        return render(request, 'error.html')
    
    return HttpResponseRedirect('/board/list')  #수정 후 목록보기


def DeleteFunc(request):
    try:
        data = BoardTab.objects.get(id = request.GET.get('id'))
    except Exception as e:
        print('DeleteFunc error: ' , e)
    
    return render(request, 'delete.html', {'data_one':data})


def DeleteOkFunc(request):
    delRec = BoardTab.objects.get(id=request.POST.get('id'))

    if delRec.passwd == request.POST.get('del_passwd'):  #비밀번호가 일치하면 삭제
        delRec.delete()
        return HttpResponseRedirect('/board/list')  #삭제 후 목록보기
    
    else:
        return render(request, 'error.html')
    
    
def SearchFunc(request):
    if request.method == "POST":
        s_type = request.POST.get('s_type')
        s_value = request.POST.get('s_value')
        #print(s_type, ' ', s_value)
        if s_type == 'title':
            datas = BoardTab.objects.filter(title__contains = s_value).order_by('-id')
        elif s_type == 'name':
            datas = BoardTab.objects.filter(name__contains = s_value).order_by('-id')
        
        paginator = Paginator(datas, 5)  #한 화면에 5행씩 출력
        page = request.GET.get('page')
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        return render(request, 'board.html', {'data':data})  #board.html 에서 data로 받고 있기 때문에 이름을 동일하게 준다.
    
    else:
        return HttpResponseRedirect('/board/list')


def ReplyFunc(request):
    try:
        data = BoardTab.objects.get(id=request.GET.get('id'))  #댓글을 달고자 하는 원글 읽기
    
    except Exception as e:
        print('ReplyFunc error: ', e)
        
    return render(request, 'reply.html', {'data_one':data})


def ReplyOkFunc(request):
    if request.method == "POST":
        try:
            regnum = int(request.POST.get('gnum'))
            reonum = int(request.POST.get('onum'))
            
            tempRec = BoardTab.objects.get(id = request.POST.get('id')) #원글
            old_gnum = tempRec.gnum
            old_onum = tempRec.onum
            
            if old_onum >= reonum and old_gnum == regnum:
                old_onum += 1 #onum 갱신
            
            #댓글 저장
            BoardTab(
                name = request.POST.get('name'),
                passwd = request.POST.get('passwd'),
                mail = request.POST.get('mail'),
                title = request.POST.get('title'),
                cont = request.POST.get('cont'),
                bip = request.META['REMOTE_ADDR'],
                bdate = datetime.now(),
                readcnt = 0,     #초기값 0
                gnum = regnum,   #원글의 번호를 부여 -> 같은 그룹이됨 
                onum = old_onum, #소속 댓글의 번호 적용
                nested = int(request.POST.get('nested')) + 1  #들여쓰기
            ).save()
            
        except Exception as e:
            print('ReplyOkFunc error: ', e)

    
    return HttpResponseRedirect('/board/list')
