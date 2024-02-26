from django.urls import path
from MyApp import views

urlpatterns=[
    path('',views.home, name='my_home'),
    path('about/',views.about, name='my_about'),
    path('pricing/', views.pricing, name='my_pricing'),
    path('services/', views.services, name='my_services'),
    path('contact/', views.contact, name='my_contacts')
]
