from django.urls import path
from . import views

app_name = 'BTS'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('album_index/', views.album_index, name='album_index'),
    path('album_index_create/', views.album_index_create, name='album_index_create'),
    path('detail/<int:pk>/',views.detail, name = 'detail'),
    path('album_detail/<int:pk>/',views.album_detail, name = 'album_detail'),
    path('<int:pk>/delete/',views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name = 'update'),
]
