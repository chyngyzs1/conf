from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import SendSubForm
from .models import SendSubmission
from .function import handle_upload_file



# @login_required(login_url='login_page')

def index(request):
    return render(request, 'pages/home.html')



def registerPage(request):
    if request.method == "POST":
        username = request.POST['name'].lower()
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirmPassword']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'User with this username already exists!')
                return redirect('register_page')
            else:
                user = User.objects.create_user(password=password1, email=email, username=username)
                user.save()
                return redirect('login_page')
        else:
            messages.error(request, "passwords doesn't match")

    return render(request, 'pages/registration.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('email').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'username or password is incorrect!')

    context = {}
    return render(request, 'pages/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home_page')



@login_required(login_url='login_page')
def sendform(request):
    if request.method == 'POST':
        form = SendSubForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            # form.save()
            messages.success(request, 'Form is accepted!')
            return redirect('home_page')
    else:
        form = SendSubForm()
    context = {'form': form}
    return render(request, 'pages/send_sub.html', context)




def user_room(request):

    context = {
        'list_forms': SendSubmission.objects.filter(user__username=request.user).order_by('-id')
    }
    return render(request, 'pages/user_room.html', context)


def update_form(request, pk):
    get_form = SendSubmission.objects.get(pk=pk)
    if request.method == 'POST':
        form = SendSubForm(request.POST, instance=get_form)
        if form.is_valid():
            form.save()
            return redirect('user_room')
    context = {
        'get_form': get_form,
        'update': True,
        'form': SendSubForm (instance=get_form),
    }
    return render(request, 'pages/user_room.html', context)


def delete_form(request, pk):
    get_form = SendSubmission.objects.get(pk=pk)
    get_form.delete()

    return redirect(reverse('user_room'))

def committee(request):
    return render(request, 'pages/committee.html')

def speakers(request):
    return render(request, 'pages/speakers.html')

def abstempl(request):
    return render(request, 'pages/abstractTemplate.html')

def impdate(request):
    return render(request, 'pages/importantDates.html')

def conftopic(request):
    return render(request, 'pages/conferenceTopics.html')

def particip(request):
    return render(request, 'pages/participiants.html')

def proceeding(request):
    return render(request, 'pages/proceedings.html')

def kyrgyzstan(request):
    return render(request, 'pages/aboutKyrgyzstan.html')

def history_madea(request):
    return render(request, 'pages/historyofmadea.html')

def gallery(request):
    return render(request, 'pages/gallery.html')

def contacts(request):
    return render(request, 'pages/contacts.html')

