from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', user_register, name='user_register'),
    path('login/', user_login, name='user_login'),
    path('change-password/', change_pass, name='change_pass'),
    path('logout/', user_logout, name='user_logout'),

    path('profile/', profile_view, name='profile_view'),
    path('add-calorie/', add_calorie, name='add_calorie'),
    path('calorie-calculation/', calorie_calculation, name='calorie_calculation'),
    path('delete-calorie/<int:id>/', delete_calorie, name='delete_calorie'),
    path('dashboard/', dashboard, name='dashboard'),
]