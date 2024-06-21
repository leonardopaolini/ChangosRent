from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('customer/signup', views.select_customer_type, name='signup_customer'),
    path('customer/signup/person', views.signup_person, name='signup_person'),
    path('customer/signup/company', views.signup_company, name='signup_company'),
    path('vehicle_type/create', views.create_vehicle_type, name='create_vehicle_type'),
    path('vehicle_type/edit/<int:vehicle_type_id>', views.edit_vehicle_type, name='edit_vehicle_type'),
    path('vehicle_type/list', views.list_vehicle_type, name='list_vehicle_type'),
]
