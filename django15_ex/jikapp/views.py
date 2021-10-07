from django.shortcuts import render
from jikapp.models import Jikwon, Buser
from django.http.response import HttpResponse
import json

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def ListFunc(request):
    jik = request.GET['jik']
    jdata = Jikwon.objects.values('jikwon_no','jikwon_name','buser_num').filter(jikwon_jik=jik)
    bdata = Buser.objects.values('buser_no','buser_name')
    #print(jik)
    #print(jdata)
    #print(bdata)
    
    data_list=[]
    for j in jdata:
        for b in bdata:
            if j['buser_num'] == b['buser_no']:
                j['buser_name'] = b['buser_name']
        data_list.append(j)
    print(data_list)
        
    return HttpResponse(json.dumps(data_list), content_type="application/json")

