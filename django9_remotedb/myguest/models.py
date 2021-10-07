from django.db import models

# Create your models here.
class Guest(models.Model):
    #myno = models.AutoField(auto_created=True, primary_key=True)  #id가 생성되지 않고 프라이머리 키를 직접 생성
    title = models.CharField(max_length=50)
    content = models.TextField()  #많은 양의 데이터를 가져올 수 있다. 허용하는 만큼 
    regdate = models.DateTimeField()
    
    #정렬 방법 2  #정렬하고 나서는 migration 할 필요 없다
    class Meta:  
        #ordering = ('title',)  #tuple 형태이므로 ',' 필수
        #ordering = ('-title', 'id')
        ordering = ('-id',)  #최근 입력된 순서대로
    