from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('customer/signup/person', views.signup_person, name='signup_person'),
    path('customer/signup/company', views.signup_company, name='signup_company'),
    path('customer/signup/person/edit/<int:person_id>', views.edit_person, name='edit_person'),
    path('customer/signup/company/edit/<int:company_id>', views.edit_company, name='edit_company'),
    path('customer/list', views.list_customer, name='list_customer'),
    path('vehicle_type/create', views.create_vehicle_type, name='create_vehicle_type'),
    path('vehicle_type/edit/<int:vehicle_type_id>', views.edit_vehicle_type, name='edit_vehicle_type'),
    path('vehicle_type/list', views.list_vehicle_type.as_view(), name='list_vehicle_type'),
    path('vehicle/create', views.create_vehicle, name='create_vehicle'),
    path('vehicle/edit/<int:vehicle_id>', views.edit_vehicle, name='edit_vehicle'),
    path('vehicle/list', views.list_vehicle, name='list_vehicle'),
    path('rent/create', views.create_rent, name='create_rent'),
    path('rent/list', views.list_rent, name='list_rent'),
    path('rent/customer/list', views.list_rent_by_customer, name='list_rent_by_customer'),
    path('account/password/reset/request', views.request_for_password_reset, name='request_password_reset'),
    path('account/password/reset/request/<str:uid>/<str:token>', views.reset_password, name='reset_password'),
    path('account/profile', views.account_profile, name='account_profile'),

]
