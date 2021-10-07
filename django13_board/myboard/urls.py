from django.urls import path
from myboard import views

urlpatterns = [
    path(r'list', views.ListFunc),
    path(r'insert', views.InsertFunc),
    path(r'insertok', views.InsertOkFunc),
    path(r'content', views.ContentFunc),
    path(r'update', views.UpdateFunc),
    path(r'updateok', views.UpdateOkFunc),
    path(r'delete', views.DeleteFunc),
    path(r'deleteok', views.DeleteOkFunc),
    path(r'search', views.SearchFunc),
    
    path(r'reply', views.ReplyFunc),
    path(r'replyok', views.ReplyOkFunc),
    
]