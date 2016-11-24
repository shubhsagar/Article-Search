from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def login(request):
	return render(request, 'webD/login.html', {'question': "myquestions"})

def home(request):
    username = request.session.get('S_username', 'DEFAULT')
    if username == "DEFAULT" :
        uname = request.GET.get('uname', '')
        context = {
        	'name': uname
        }
        request.session['S_username'] = uname
        username = request.session.get('S_username', 'DEFAULT')
    return render(request, 'webD/home.html', {'username': username})

def signup(request):
    return render(request, 'webD/signup.html', {'username': 'username'} )


def readlist(request):
    username = request.session.get('S_username', 'DEFAULT')
    return render(request, 'webD/readlist.html', {'username': username} )


def history(request):
    username = request.session.get('S_username', 'DEFAULT')
    return render(request, 'webD/history.html', {'username': username})

def logout(request):
    request.session['S_username'] = "DEFAULT"
    return render(request, 'webD/logout.html', {'question': "myquestions"})
