from django.shortcuts import render
#from webD.models import Student

# Create your views here.
from django.http import HttpResponse

# def login(request):
# 	return render(request, 'webD/login.html', {'question': "myquestions"})

def login(request):
    if request.method == "POST":            #when username & password is typed
        print ("login post request")
        uname = request.POST.get('uname', '')
        password = request.POST.get('password', '')
        user_verification = False
        
        #check if the username and password in database
        if Student.objects.filter(Username=uname, Password=password).exists():
            user_verification = True

        if user_verification:
            context = {
            'name': uname
            }
            request.session['S_username'] = uname
            username = request.session.get('S_username', 'DEFAULT')
            return render(request, 'webD/home.html', {'username': username})

        else:
            return render(request, 'webD/login.html', {'question': "myquestions"})
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
    if request.method == "POST":
        #save deatails in the database
        print ("signup post request")
        uname = request.POST.get('uname', '')
        email = request.POST.get('emaild', '')
        password = request.POST.get('pass', '')
        
        newStudent = Student(Username=uname, EmailID = email, Password = password)
        newStudent.save()        
        return render(request, 'webD/login.html', {'question': "myquestions"})

    return render(request, 'webD/signup.html', {'username': 'username'} )

# def addStudent(request):
#     name = request.POST["name"]
#     email = request.POST["email"]
#     password = request.POST["pass"]
#     print ("name :",name)
#     print ("email :",email)
#     print ("password :",password)
#     print ("student details recorded, now send them to the database..")

def readlist(request):
    username = request.session.get('S_username', 'DEFAULT')
    return render(request, 'webD/readlist.html', {'username': username} )


def history(request):
    username = request.session.get('S_username', 'DEFAULT')
    return render(request, 'webD/history.html', {'username': username})

def logout(request):
    request.session['S_username'] = "DEFAULT"
    return render(request, 'webD/logout.html', {'question': "myquestions"})
