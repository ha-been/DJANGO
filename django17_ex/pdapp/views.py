from django.shortcuts import render
from pdapp.models import Jikwon, Buser
import pandas as pd
from datetime import datetime, date
from pandas.core.reshape.pivot import crosstab
import matplotlib.pyplot as plt

# Create your views here.
def MainFunc(request):
    
    return render(request, 'main.html')


def showData(request):
    
    jikwon = pd.DataFrame.from_records(Jikwon.objects.all().values())
    buser = pd.DataFrame.from_records(Buser.objects.all().values())
    mergejb = pd.merge(jikwon, buser[['buser_no','buser_name']], left_on='buser_num', right_on='buser_no', how='left')
    mergejb = mergejb.drop('buser_no', axis=1)
    mergejb.columns = ['사번','직원명','부서번호','직급','연봉','입사일','성별','평가','부서명']
    #print(mergejb)

    #1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오.
    mergejb['근무년수'] = (date.today()-mergejb['입사일'])
    con1 = mergejb[['사번','직원명','부서명','직급','연봉','근무년수']]
    
    #2) 부서명, 직급 자료를 이용하여  각각 급여합, 급여평균을 구하시오. 
    buser_group = mergejb['연봉'].groupby(mergejb['부서명'])
    buser_group_detail = {'sum':buser_group.sum(), 'avg':buser_group.mean()}
    print(buser_group_detail)
    
    #3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.  
    bu_result = buser_group.agg(['sum','mean'])
    bu_result.plot(kind='barh')
    plt.rc('font', family='malgun gothic')
    plt.title('부서별 연봉합, 연봉평균')
    fig = plt.gcf()
    fig.savefig('django17_ex/pdapp/static/images/graph.png')
    
    #4) 성별, 직급별 빈도표를 출력하시오. 
    cross = crosstab(mergejb['성별'],mergejb['직급'])
    
    return render(request, 'list.html', {'con1':con1.to_html(), 'con2':buser_group_detail, 'con4':cross.to_html()})

