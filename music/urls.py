from django.urls import path
from . import views

app_name = 'music'
urlpatterns =[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('song/<int:pk>/', views.SongView.as_view(), name='song_detail'),
    path('song/<int:song_id>/save/',views.save_song,name='save_song'),
]