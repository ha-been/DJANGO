from django.shortcuts import render
from jikapp.models import Jikwon, Buser
from django.http.response import HttpResponse
import json

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def ListFunc(request):
    jik = request.GET['jik']
    data = Jikwon.objects.extra(tables=['Buser'], where=['Buser.buser_no=buser_num'])
    print(data)
    print(jik)
    
    data_list=[]
    for d in data:
        data_list.append(d)
        
    return HttpResponse(json.dumps(data_list), content_type="application/json")