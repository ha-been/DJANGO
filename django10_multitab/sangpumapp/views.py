from django.shortcuts import render
from sangpumapp.models import Maker, Product
import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'sangpumdb',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

# Create your views here.
def Main(request):
    return render(request, 'main.html')

def List1(request):
    #장고의 ORM 사용
    makers = Maker.objects.all()
    print(type(makers))   # <class 'django.db.models.query.QuerySet'>
    
    #python 기본 DB 연결처리
    # conn=MySQLdb.connect(**config)
    # cursor=conn.cursor()
    # cursor.execute("select * from sangpumapp_maker")
    # makers = cursor.fetchall()
    # print(type(makers))  # <class 'tuple'> 튜플타입으로 넘어오기 때문에 html에서 받을 때 다르게 처리 해주어야 한다.
    # cursor.close()
    # conn.close()
        
    return render(request, 'list1.html', {'makers':makers})

def List2(request):
    products = Product.objects.all()
    pcount = len(products)
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})

def List3(request):
    mid = request.GET.get('id')
    products = Product.objects.filter(maker_name=mid)
    pcount = len(products)
    
    return render(request, 'list2.html', {'products':products, 'pcount':pcount})