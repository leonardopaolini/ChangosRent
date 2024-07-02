from django.shortcuts import redirect
from webapp.models import Person, Company
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from webapp.common.api.email_api_client import EmailMessage


def redirect_to_home():
    return redirect('home')


def redirect_to_login():
    return redirect('login')


def find_user_by_email(email):
    customer = Person.objects.filter(email=email).first()
    if not customer:
        customer = Company.objects.filter(email=email).first()
    if not customer:
        raise User.DoesNotExist(f'User with email {email} not found')
    return customer.user


def find_customer_by_user(user):
    customer = Person.objects.filter(user=user).first()
    if not customer:
        customer = Company.objects.filter(user=user).first()
    if not customer:
        raise User.DoesNotExist(f'Customer for User {user.username} not found')
    return customer


def reset_password_request_message(request, user, email):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    uri = f'/{uid}/{token}'
    reset_url = request.build_absolute_uri() + uri
    return (EmailMessage.reset_password_request_message_builder()
            .set_user(user)
            .set_email(email)
            .set_reset_url(reset_url)
            .build())


def decode_password_reset_request_user(uid):
    return User.objects.get(id=urlsafe_base64_decode(uid).decode())


def sign_up_person_message(person, user):
    return (EmailMessage.sign_up_person_message_builder()
                        .set_user(user)
                        .set_email(person.email)
                        .set_first_name(person.first_name)
                        .set_last_name(person.last_name)
                        .build())


def sign_up_company_message(company, user):
    return (EmailMessage.sign_up_company_message_builder()
                        .set_user(user)
                        .set_email(company.email)
                        .set_business_name(company.business_name)
                        .build())
