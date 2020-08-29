from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')


# def custom_sign_in(request):
#     return render(request, 'sign-in.html')
