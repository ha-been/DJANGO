from django.shortcuts import render
from jikwon.models import Jikwon
import pandas as pd
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from django.http.response import JsonResponse


# Create your views here.
def Main(request):

    return render(request, 'main.html')


@csrf_exempt
def Predict(request):
    #근무년수 받기
    year = request.POST['year']
    new_val = pd.DataFrame({'year':[year]})
    
    datas = Jikwon.objects.values('jikwon_ibsail','jikwon_pay','jikwon_jik').all()
    jikwon = pd.DataFrame.from_records(datas)
    
    #근무년수 구하기
    for i in range(len(jikwon['jikwon_ibsail'])):
        jikwon['jikwon_ibsail'][i] = int((datetime.now().date()-jikwon['jikwon_ibsail'][i]).days/365)
    jikwon.columns = ['근무년수','연봉','직급']
    #print(jikwon)
    
    #데이터셋 나누기
    train_set, test_set = train_test_split(jikwon, test_size = 0.2)
    #print(train_set.shape, test_set.shape)
    
    #모델 작성
    model_lr = LinearRegression().fit(X = train_set.iloc[:,[0]], y = train_set.iloc[:,[1]])
    
    #성능 확인
    ##예측값으로 성능 평가
    test_pred = model_lr.predict(test_set.iloc[:,[0]][:5])
    test_real = test_set.iloc[:,1][:5]
    print('예측값:\n', test_pred)
    print('실제값:\n', test_real)
    #성능은 별로인듯... 
    
    ##rmse로 성능 평가
    lin_mse = mean_squared_error(test_real, test_pred)
    lin_rmse = np.sqrt(lin_mse)
    print('RMSE:', lin_rmse)  #1068.91
    #역시 성능은 별로... 
    
    #새로운 값 예측
    new_pred = round(model_lr.predict(new_val)[0][0], 2)
    #print(new_pred)
    
    #직급별 연봉 평균
    pay_jik = jikwon.groupby('직급').mean().round(1)
    pay_jik2 = pay_jik.to_html()
    
    
    return JsonResponse({'success': True, 'new_pred':new_pred, 'pay_jik':pay_jik2})
    
    
