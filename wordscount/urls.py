from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name='index'),
#wordscount/
path('count/',views.count,name='count'),
#wordscount/count/
]

