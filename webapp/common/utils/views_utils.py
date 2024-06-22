from django.shortcuts import redirect


def get_menu(request):
    if request.user.is_staff:
        return 'admin/menu/menu.html'
    return 'customer/menu/menu.html'


def redirect_to_home():
    return redirect('home')


def redirect_to_login():
    return redirect('login')

