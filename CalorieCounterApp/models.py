from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=[('', 'Select Gender'), ('Male', 'Male'), ('Female', 'Female')])
    height = models.FloatField(help_text='Height in cm')
    weight = models.FloatField(help_text='Weight in kg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_bmr(self):
        if self.gender == 'Male':
            bmr = (66.47+(13.75 * self.weight)+(5.003 * self.height)-(6.755 * self.age))
        elif self.gender == 'Female':
            bmr = (655.1+(9.563 * self.weight)+(1.850 * self.height)-(4.676 * self.age))
        else:
            return 0
        return round(bmr, 2)
        
    def __str__(self):
        return self.name

class ConsumedCalorie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consumed_calories')
    item_name = models.CharField(max_length=150)
    calorie_consumed = models.FloatField()
    date = models.DateField(default=timezone.localdate)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item_name} - {self.calorie_consumed} kcal"