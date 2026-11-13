
from django.urls import path

from mainapp import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contacts/',views.contact,name='contact'),
]