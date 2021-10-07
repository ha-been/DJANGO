from django.db import models

# Create your models here.  테이블을 클래스로 정의
class Article(models.Model):   #models.Model을 상속
    #컬럼은 속성으로 정의
    code = models.CharField(max_length=10)  #고정된 문자열
    name = models.CharField(max_length=20)
    
    price = models.IntegerField() #정수 자료형
    pub_date = models.DateTimeField()
    
    #EmailField, DateTimeField, TextField ...