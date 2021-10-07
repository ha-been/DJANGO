from django.shortcuts import render
from ormapp.models import Profile
from django.db.models.aggregates import Avg, Sum, Max,Min, Count, StdDev,Variance

# Create your views here.

def IndexFunc(request):
    return render(request, 'index.html')

def CalldictFunc(request):
    profile_list = Profile.objects.all()
    print(profile_list)
    
    #for row in profile_list.values():
    for row in profile_list.values_list():
        print(row)
        
    # 소계_console에 찍히는것
    print(Profile.objects.aggregate(Avg('age')))
    print(Profile.objects.aggregate(Sum('age')))
    print(Profile.objects.aggregate(Max('age')))
    print(Profile.objects.aggregate(Count('age')))
    
    #where 조건
    print(Profile.objects.filter(name='홍길동'))
    print(Profile.objects.filter(name='홍길동').aggregate(Avg('age')))
    print(Profile.objects.exclude(name='홍길동').aggregate(Avg('age')))  #홍길동 제외
    print(Profile.objects.values('name').distinct())
    
    #values() + annotate() 그룹별
    #print(Profile.objects.values('name').annotate(Avg('age')))
    qs = Profile.objects.values('name').annotate(Avg('age'))  #나이별 그룹
    for r in qs:
        print(r)
        
    pro_list = []
    for pro in profile_list:
        pro_dict = {}
        pro_dict['name'] = pro.name
        pro_dict['age'] = pro.age
        pro_list.append(pro_dict)
        print(pro_list)
    
    context = {'pro_dict':pro_list}
    
    return render(request, "show.html", context)



