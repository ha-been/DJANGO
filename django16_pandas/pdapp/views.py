from django.shortcuts import render
from pdapp.models import Jikwon
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

# Create your views here.
def mainFunc(request):
    return render(request, 'main.html')


def dispFunc(request):
    datas = Jikwon.objects.all().values()
    #print(datas)
    
    pd.set_option('display.max_columns', 500)
    df = pd.DataFrame.from_records(datas)
    df.columns = ['사번','직원명','부서','직급','연봉','입사','성별','평가']
    print(df.head(3))
    
    #그룹별 작업
    buser_group = df['연봉'].groupby(df['부서'])
    print(buser_group.sum())
    
    buser_group_detail = {'sum':buser_group.sum(), 'avg':buser_group.mean()}
    print(buser_group_detail)
    
    #시각화 결과 파일로 저장
    bu_result = buser_group.agg(['sum','mean'])
    print(bu_result, type(bu_result))
    bu_result.plot(kind='barh')
    plt.title('부서별 연봉합, 연봉평균')
    fig = plt.gcf()
    fig.savefig('django16_pandas/pdapp/static/images/test.png')
    
    return render(request, 'list.html', {'datas':df.to_html(), 'buser_group':buser_group_detail})



