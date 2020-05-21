from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('create/', views.create_article, name='create_article'),
    path('<int:article_pk>/', views.article_detail, name='article_detail'),
    path('<int:article_pk>/update/', views.update_article, name='update_article'),
    path('<int:article_pk>/delete/', views.delete_article, name='delete_article'),
    path('<int:article_pk>/comment/create/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/<int:comment_pk>/comment/update/', views.update_comment, name='update_comment'),
    path('<int:article_pk>/<int:comment_pk>/comment/delete/', views.delete_comment, name='delete_comment'),
    path('<int:article_pk>/like/', views.like_article, name='like_article'),
]