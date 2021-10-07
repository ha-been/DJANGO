from django.shortcuts import render
import json
from django.http.response import HttpResponse
    
# Create your views here.
lan = {
    'id':111,
    'name':'파이썬',
    'history':[
        {'date':'2021-5-1','py':'basic'},
        {'date':'2021-6-1','py':'django'}
    ]
}
#print(type(lan))

def test():
    #JSON 인코딩 : python의 객체를 문자열로 변환
    print(type(lan))   #dict
    jsonString = json.dumps(lan)  #string type으로 변환
    print(type(jsonString))   #str
    print(jsonString)
    
    jsonString2 = json.dumps(lan, indent = 4)
    print(jsonString2)
    
    #JSON 디코딩 : 문자열을 python의 객체로 변환
    dicData = json.loads(jsonString)
    print(type(dicData))  #<class 'dict'>
    print(dicData['name'])
    for h in dicData['history']:
        print(h['date'],' ',h['py'])


def IndexFunc(request):
    #test()
   
    return render(request, 'abc.html')

import time
def func1(request):
    msg = request.GET['msg']  #msg = request.GET.get('msg')
    #print(msg)
    msg += "만세"
    context = {'key':msg}
    #time.sleep(5)  #일부러 시간주기. 비동기방식이기 때문에 처리하는 동안 다른 작업 가능

    return HttpResponse(json.dumps(context), content_type = "application/json")  
    #render하면 안됨! HttpResponse object를 받음
    #HttpResponse:클라이언트에게 요청을 전송?, HttpRequest: 클라이언트의 요청을 받는것
    #content_type =  mime type을 적어준다.
    

def func2(request):
    datas = [
        {'irum':'홍길동','nai':22},
        {'irum':'고길동','nai':34},
        {'irum':'나길동','nai':52}
        
    ]
    
    return HttpResponse(json.dumps(datas), content_type = "application/json")


def func3(request):
    msg = request.GET['msg']
    msg = msg + " 너무 시끄러워"
    context = {'key':msg}
    
    return HttpResponse(json.dumps(context), content_type = "application/json")  


def func4(request):
    datas = [
        {'irum':'방국봉','nai':25},
        {'irum':'방상','nai':38},
        {'irum':'방방','nai':54}
        
    ]
    
    return HttpResponse(json.dumps(datas), content_type = "application/json")


def func5(request):
    pass


