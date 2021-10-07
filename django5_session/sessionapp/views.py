from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from gevent.libev.corecext import NONE

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')


def setosFunc(request):
    if 'favorite_os' in request.GET:
        #print(request.GET['favorite_os'])
        request.session['f_os'] = request.GET['favorite_os']  #f_os라는 키로 선택된 os값이 세션에 저장.
        #return render(request, 'showos.html')   #forward 방식: client의 요청X 서버에서 바로 c로 전송. urls.py를 만나지 않음
        return HttpResponseRedirect('/showos/')  #redirect 방식: c의 요청에 의해서 urls.py를 만나 호출한 방식. html에서 <a href>해준 것과 동일
    else:
        return render(request, 'setos.html')


def showosFunc(request):
    context = {}  #dict
    if 'f_os' in request.session:
        context['f_os'] = request.session['f_os']
        context['message'] = '선택한 운영체제는 %s'%request.session['f_os']
    else:
        context['f_os'] = None
        context['message'] = '운영체제를 선택하지 않았네요'
    
    request.session.set_expiry(5)  #showosFunc를 만나고 5초 후에 세션 해제
    return render(request, 'showos.html', context)  #context는 {'f_os':값, 'message':값}
        

