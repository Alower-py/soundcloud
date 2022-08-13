from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),

    path('release', views.Album_list.as_view(), name="releases"),
    path('releases/<slug:slug>/', views.Album_detail.as_view(), name="release_detail"),

    path('tracks/<slug:slug>/', views.Tracks_detail.as_view(), name="tracks_detail"),
]
