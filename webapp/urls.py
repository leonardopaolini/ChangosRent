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
    path('vehicle/create', views.create_vehicle, name='create_vehicle'),
    path('vehicle/edit/<int:vehicle_id>', views.edit_vehicle, name='edit_vehicle'),
    path('vehicle/list', views.list_vehicle, name='list_vehicle'),
    path('rent/create', views.create_rent, name='create_rent'),
    path('rent/list', views.list_rent, name='list_rent'),
]
