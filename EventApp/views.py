from django.shortcuts import render, redirect
from .models import Event, Contact
from .forms import BookingForm
from django.contrib.auth.models import User, auth
from django.contrib import messages


def reg_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')  # Corrected typo

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('user')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already taken")
                return redirect('user')
            else:
                user_reg = User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.info(request, "Successfully registered")
                return redirect('user_login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('user')
    return render(request, 'reg.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request, "Successfully Logged")
            return redirect('/')
        else:
            messages.info(request, "Please register your account")
            return redirect('user')
    return render(request, "login.html")


def user_logout(request):
    auth.logout(request)
    return redirect('user')


def home(request):
    return render(request, 'home_page.html')


def events(request):
    dict_eve = {
        'eve': Event.objects.all()
    }
    return render(request, 'events_page.html', dict_eve)


def about(request):
    return render(request, 'about_page.html')


def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = BookingForm()
    dict_form = {'form': form}
    return render(request, 'booking_page.html', dict_form)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Create a new Contact object and save it to the database
        contact = Contact(name=name, email=email, message=message)
        contact.save()
        return redirect('contact')
    return render(request, 'contact_page.html')


# def contact_form(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         data = Contact(name=name, email=email, message=message)
#         data.save()
#         return redirect('contact')

