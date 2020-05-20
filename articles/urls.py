from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
]