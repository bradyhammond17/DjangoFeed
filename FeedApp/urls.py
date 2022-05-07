from django.urls import path
from . import views

app_name = 'FeedApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('myfeed',views.myfeed, name='myfeed'),
    ]

    