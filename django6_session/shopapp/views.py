from django.shortcuts import render

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')

def page1Func(request):
    return render(request, 'page1.html')

def page2Func(request):
    return render(request, 'page2.html')

def cartFunc(request):
    name = request.POST['name']
    price = request.POST['price']
    #하나의 상품은 품명과 가격으로 구성
    product = {'name':name, 'price':price}
    
    productList = []
    #장바구니 상품 키는 'shop'
    if 'shop' in request.session:
        productList = request.session['shop']
        productList.append(product)
        request.session['shop'] = productList
    else:
        productList.append(product)
        request.session['shop'] = productList
    
    print(productList)
    context = {}
    context['products'] = request.session['shop']
    return render(request, 'cart.html', context)

def buyFunc(request):
    if 'shop' in request.session:
        productList = request.session['shop']
        total = 0
        for pro in productList:
            total += int(pro['price'])
        
        request.session.clear()   #모든 세션 제거
        #del request.session['shop'].clear()  #특정 세션 제거
        
    return render(request, 'buy.html', {'total':total})    
    







