from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the referral system API! Use /api/ for endpoints.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('referrals.urls')),  # Указываем путь до вашего приложения
    path('', home),  # Главная страница
]
