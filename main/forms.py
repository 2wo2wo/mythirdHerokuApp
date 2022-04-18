from multiprocessing.connection import Client
from django.forms import ModelForm
from .models import Client , Meal

class AddLogins(ModelForm):
    class Meta:
        model = Client
        fields = ['id' , 'User_id' , 'name']


class MealsForm(ModelForm):
    class Meta:
        model = Meal
        fields = ['id' , 'name', 'price' , 'info']
