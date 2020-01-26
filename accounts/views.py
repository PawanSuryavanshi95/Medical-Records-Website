from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from . models import PatientProfile,DoctorProfile

# Create your views here.
def register2(request):
    if (request.method == 'POST'):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        mobile = request.POST['mobile']
        experience = request.POST['exp']

        if (password1 == password2):
            if User.objects.filter(username=username).exists():
                print('Username already exists.')
                return redirect('register2')
            else:
                print('User created.')
                person = User.objects.create_user(username=username,
                                                password=password1)
                person.save()
                doctor = DoctorProfile.objects.create(firstname=firstname,lastname=lastname,user=person,
                                                           mobile=mobile,email=email,experience=experience)
                doctor.save()
                return redirect('login')
        else:
            print('''Passwords don't match''')
            return redirect('register2')
    else:
        return render(request, r'textured_blue\register2.html')

def register1(request):
    if(request.method=='POST'):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        mobile = request.POST['mobile']
        address = request.POST['address']

        if(password1==password2):
            if User.objects.filter(username=username).exists():
                print('Username already exists.')
                return redirect('register1')
            else:
                print('User created.')
                person = User.objects.create_user(username=username,password=password1)
                person.save()
                patient = PatientProfile.objects.create(firstname=firstname,lastname=lastname,user=person,mobile=mobile,email=email,address=address)
                patient.save()
                return redirect('login')
        else:
            print('''Passwords don't match''')
            return redirect('register1')
    else:
        return render(request,r'textured_blue\register1.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            print('Loged In')
            return redirect('/home')
        else :
            print("Invalid Credentials")
            return redirect('login')
    else :
        return render(request,'textured_blue\login.html')
def logout(request):
    auth.logout(request)
    return redirect('/home')