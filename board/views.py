from django.shortcuts import render
from form import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout as signout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from board.models import Board, Task
from django.contrib.auth import REDIRECT_FIELD_NAME

# Create your views here.
def signup(request):
	if request.method=='GET':
		form = RegistrationForm()
		return render(request, 'board/signup.html', {'form': form})
	else:
		if request.method=='POST':
			form = RegistrationForm(request.POST)
			if form.is_valid():
				if form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
					return render(request, 'board/signup.html', {'form': RegistrationForm(), 'error': 'Passwords do not match'})
				form.save()
				user = User.objects.get(username = form.cleaned_data['username'])
				user.set_password(form.cleaned_data['password'])
				user.save()
				user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
				if user is not None:	
					login(request, user)
				return HttpResponseRedirect(reverse('board:index'))


def Login(request):
	#print request.user.is_authenticated()
	if request.user.is_authenticated():
		return HttpResponseRedirect(reverse('board:index'))

	if request.method=='GET':
		form = LoginForm()
		return render(request, 'board/login.html', {'form': form})
	else:
		if request.method=='POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				user = authenticate(username=username, password=password)

				redirect_to = request.POST.get(REDIRECT_FIELD_NAME,
                                   request.GET.get(REDIRECT_FIELD_NAME, ''))
				print redirect_to

				if user is not None:	
					login(request,user)
					if request.user.is_authenticated():
						return HttpResponseRedirect(redirect_to)
				else:
					return render(request, 'board/login.html', {'form': LoginForm, 'error': 'Invalid Login'})
	

@login_required(login_url='board:login')
def index(request):
	boards = Board.objects.filter(user = request.user)
	return render(request,'board/user_boards.html', {'boards': boards})



@login_required(login_url='board:login')
def add_board(request):
	if request.method=='GET':
		form = AddBoard()
		return render(request, 'board/add_board.html', {'form': form})
	else:
		if request.method=='POST':
			form = AddBoard(request.POST)
			if form.is_valid():
				board = form.save(commit=False)	
				board.user = request.user
				board.save()
				return HttpResponseRedirect(reverse('board:index'))

def logout(request):
	signout(request)
	return HttpResponseRedirect(reverse('board:login'))	


@login_required(login_url='board:login')
def update_task(request, task_id):
	if request.method=='GET':
		return render(request, 'board/update_task.html', {'task_id': task_id})
	else:
		if request.method=='POST':
			task = Task.objects.get(id=task_id)
			task.completed_percentage = request.POST['percentage']
			task.save()
			return HttpResponseRedirect(reverse('board:index'))