from django.urls import path

from . import views
# . means same current folder

app_name = 'MainApp'

urlpatterns = [
    path('',views.index, name='index'),
    path('topics',views.topics, name='topics'),
]