import re
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password':'drgdfg3re'})

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    upper_characters = [char.upper() for char in characters]
    numbers = list('0123456789')
    special_characters = list('!@#$%^&*()')
    final_list = characters
    thepassword = ''
    length = int(request.GET.get('length', 14))
    is_upper = request.GET.get('uppercase', False)
    is_number = request.GET.get('numbers', False)
    is_special = request.GET.get('special', False)
    if is_upper:
        final_list.extend(upper_characters)
    if is_number:
        final_list.extend(numbers)
    if is_special:
        final_list.extend(special_characters)
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})