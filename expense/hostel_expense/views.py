from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from hostel_expense.models import *
import simplejson
import datetime
from decorator import check_login

# Create your views here.

def index(request):
	month = request.POST.get('month',datetime.datetime.now().month)
	year = request.POST.get('year',datetime.datetime.now().year)
	loged = 'f'
	username = ''
	if request.session.has_key('user'):
		username = request.session['user']
		loged = 't'
	expense = Expense.objects.filter(date__month=month, date__year=year).order_by('-date')
	total = 0
	for e  in expense:
		total += float(e.amount)
	exp = []
	for e in expense:
		ep={}
		ep['user'] = e.user.username
		ep['amount'] = e.amount
		ep['date'] = e.date
		ep['description'] = e.description
		exp.append(ep)

	return render(request, 'index.html', {"expense":exp, "total":total, "loged":loged, "username":username,"month":month})

def chart(request):
	month = request.POST.get('month',datetime.datetime.now().month)
	year = request.POST.get('year',datetime.datetime.now().year)
	expense = Expense.objects.filter(date__month=month, date__year=year).order_by('date')
	data = []
	for e in expense:
		k={}
		t = 0
		for i in data:
			if i['date'] == str(e.date.strftime("%Y-%m-%d ")):
				i['close'] += int(e.amount)
				t = 1
				continue
		if not t:
			k['date'] = str(e.date.strftime("%Y-%m-%d "))
			k['close'] = int(e.amount)
			data.append(k)
	return render(request, 'chart.html', {'data': data,"month":month})


def month_chart(request):
	year = request.POST.get('year',datetime.datetime.now().year)
	expense = Expense.objects.filter(date__year=year).order_by('date')
	data = []
	for e in expense:
		k={}
		t = 0
		for i in data:
			if i['month'] == e.date.strftime("%B"):
				i['amount'] += int(e.amount)
				t = 1
				continue
		if not t:
			k['month'] = e.date.strftime("%B")
			k['amount'] = int(e.amount)
			data.append(k)
	return render(request, 'month_chart.html', {'data': data})

def login(request):
	return render(request, 'login.html', {})

def authenticate(request):
	try:

		username = request.POST['username']
		password = request.POST['password']

		user = User.objects.get(username=username, password=password)
		request.session['user'] = user.username
		expense = Expense.objects.all().order_by('-date')
		total = 0
		for e  in expense:
			total += float(e.amount)
		exp = []
		for e in expense:
			ep={}
			ep['user'] = e.user.username
			ep['amount'] = e.amount
			ep['date'] = e.date
			ep['description'] = e.description
			exp.append(ep)
		return HttpResponseRedirect('/')
	except:
		return render(request, 'login.html', {"error":"Username or password not match"})

def add_expense(request):
	if request.method == 'POST':
		username = request.session['user']
		date = request.POST['date']
		description = request.POST['description']
		amount = request.POST['amount']
		user = User.objects.get(username=username)
		date = datetime.datetime.strptime(date, "%Y-%m-%d")
		expense = Expense()
		expense.user = user
		expense.date = date
		expense.description = description
		expense.amount = amount
		expense.save()
		return render(request, 'add_expense.html', {"message":"Expense added..."})
	else:
		return render(request, 'add_expense.html', {})

def individual_expense(request):
	users = User.objects.all()
	expense_list = []
	for user in users:
		total = 0
		expense = Expense.objects.filter(user=user)
		print expense
		for e in expense:
			total += int(e.amount)
		ppp = {}
		ppp['user'] = user.username
		ppp['amount'] = total
		expense_list.append(ppp)
	return render(request, 'show_individual.html', {"expense_list":expense_list})





