
from django.urls import path
from.import views

urlpatterns = [
    path('', views.home,name="home"),
    path('landlord/', views.landlord,name="landlord"),
    path('tenant/', views.tenant,name="tenant"),    
]