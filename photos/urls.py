from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.photo_list, name='photo_list'),
    path('create/', views.create_photo, name='create_photo'),
    path('<int:photo_pk>/', views.photo_detail, name='photo_detail'),
    path('<int:photo_pk>/update/', views.update_photo, name='update_photo'),
    path('<int:photo_pk>/delete/', views.delete_photo, name='delete_photo'),
    path('<int:photo_pk>/comments/', views.create_comment, name='create_comment'),
    path('<int:photo_pk>/comments/<int:comment_pk>/update/', views.update_comment, name='update_comment'),
    path('<int:photo_pk>/comments/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:photo_pk>/like/', views.like_photo, name='like_photo'),
    path('<int:photo_pk>/comments/<int:comment_pk>/like/', views.like_comment, name='like_comment'),
]