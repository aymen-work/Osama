from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/',views.index,name='index'),
    path('', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path("add/",views.add_product, name="add"),
]
