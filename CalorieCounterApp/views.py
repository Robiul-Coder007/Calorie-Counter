from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.utils import timezone
from django.db.models import Sum
from .forms import *
from .models import *

def homepage(request):
    return render(request, 'homepage.html', {'page': 'Calorie Counter'})

def user_register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        pro_form = UserProfileForm(request.POST)
        if user_form.is_valid() and pro_form.is_valid():
            user = user_form.save()
            profile_obj = pro_form.save(commit=False)
            profile_obj.user = user
            profile_obj.save()
            
            login(request, user)
            return redirect('dashboard')
    else:
        user_form = RegistrationForm()
        pro_form = UserProfileForm()
    return render(request, 'user_register.html', {'page' : 'User Registration', 'user_form' : user_form, 'pro_form' : pro_form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() 
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'user_login.html', {'page': 'User Login', 'form' : form})

@login_required(login_url='user_login')
def change_pass(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'change_pass.html', {'page' : 'Change Password', 'form' : form})

@login_required(login_url='user_login')
def profile_view(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        profile = None
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile_obj = form.save(commit=False)
            if profile is None:
                profile_obj.user = request.user
            profile_obj.save()
            return redirect('dashboard')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'profile_view.html', {'page' : 'Profile Information', 'form' : form, 'profile' : profile})

@login_required(login_url='user_login')
def add_calorie(request): # Rice-250 kcal,# Egg-80 kcal,# Chicken-200 kcal,# Banana-100 kcal
    if request.method == 'POST':
        form = ConsumedCalorieForm(request.POST)
        if form.is_valid():
            calorie = form.save(commit=False)
            calorie.user = request.user
            calorie.save()
            return redirect('dashboard')
    else:
        form = ConsumedCalorieForm()
    return render(request, 'add_calorie.html', {'page' : 'Add Calorie', 'form' : form})

@login_required(login_url='user_login')
def calorie_calculation(request):
    try:
        profile = request.user.profile
        required_calories = profile.calculate_bmr() or 0
    except UserProfile.DoesNotExist:
        return redirect('profile_view')
    return render(request, 'calorie_calculation.html', {'page': 'Calorie Calculation', 'required_calories' : required_calories, 'profile' : profile})

@login_required(login_url='user_login')
def dashboard(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return redirect('profile_view')

    required_calories = 0
    consumed_calories = 0
    remaining_calories = 0
    progress = 0
    guideline = ""
    today = timezone.localdate()

    today_calories = ConsumedCalorie.objects.filter(
        user=request.user,
        date=today
    ).order_by('-created_at')
    
    consumed_calories = today_calories.aggregate(
        total=Sum('calorie_consumed')
    )['total'] or 0
    calorie_items = today_calories

    if profile:
        required_calories = profile.calculate_bmr() or 0
        remaining_calories = required_calories - consumed_calories
        
        if required_calories > 0:
            progress = (consumed_calories / required_calories) * 100
            progress = min(round(progress), 100)

        if consumed_calories < required_calories:
            guideline = (
                "Your calorie intake is below your estimated daily requirement. "
                "For healthy weight gain, consider eating balanced, nutritious meals."
            )
        elif consumed_calories > required_calories:
            guideline = (
                "Your calorie intake is above your estimated daily requirement. "
                "For weight management, consider balanced portions and regular physical activity."
            )
        else:
            guideline = "Your calorie intake is approximately equal to your estimated daily requirement."
    else:
        remaining_calories = 0 - consumed_calories
        guideline = "Please complete your profile to calculate your calorie requirement."
        
    context = {
        'page' : 'Dashboard',
        'profile': profile,
        'required_calories': round(float(required_calories), 2),
        'consumed_calories': round(float(consumed_calories), 2),
        'remaining_calories': round(float(remaining_calories), 2),
        'progress': progress,
        'calorie_items': calorie_items,
        'today': today,
        'guideline': guideline,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url='user_login')
def delete_calorie(request, id):
    calorie = get_object_or_404(ConsumedCalorie, id=id, user=request.user)
    calorie.delete()
    return redirect('dashboard')

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('user_login')