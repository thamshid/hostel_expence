from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from hostel_expense.models import *
def check_login(function):
    def wrapper(request, *args, **kwargs):
        try:
        	if request.session['user']:
        		pass
      
        except:
            return render(request, 'login.html')
        return function(request, *args, **kwargs)
    return wrapper