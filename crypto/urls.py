from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('fear/',views.fear,name='fear'),
    path('price/',views.price,name='price'),
    path('search/',views.search,name='search'),
]