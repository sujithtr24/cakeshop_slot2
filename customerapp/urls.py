from django.urls import path
from . import views

urlpatterns =[
    path('home/', views.home),
    path('about/',views.about, name="about-page"),
    path('home-page/', views.home_page),
    path('login-page/',views.login_page, name='login_page'),
    path('register-page/',views.register_page, name='register-page'),
    path('view-products/',views.view_products, name='view-products')
]