from django.conf.urls import url 
from first_app import views
from django.urls import path

urlpatterns = [
    path('breakfast/', views.breakfast, name="breakfast"),
    path('ngo/', views.ngo, name="ngo"),
    path('rescue/', views.rescue, name="rescue"),
    path('relief/', views.relief, name="relief"),
]
