from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm

# ----------------------------- home page -------------------------------------
def home_page(request):
  context = {
    'title': 'Golden State Towing',
  }
  if request.user.is_authenticated:
    context ['admin'] = 'You ae loged in as admin'
  return render(request, 'home_page.html', context )

# ----------------------------- about page -------------------------------------
def about_page(request):
  context = {
    'title': 'About Us',
  }
  return render(request, 'about.html', context )


# ----------------------------- contact page -------------------------------------
def contact_page(request):
  contact_form = ContactForm(request.POST or None)
  context = {
    'title': 'Contact Us',
    'form': contact_form,
  }
  if contact_form.is_valid():
    print(contact_form.cleaned_data)
  # if request.method == "POST":
  #     # print(request.POST)
  #     print(request.POST.get('full_name'))
  #     print(request.POST.get('email'))
  #     print(request.POST.get('message'))
  return render(request, 'contact/view.html', context )


# ----------------------------- login page -------------------------------------
def login_page(request):
  form = LoginForm(request.POST or None)
  context = {
    'form': form ,
    }
  print('User loged in = ')
  print(request.user.is_authenticated)
  if form.is_valid():
    print(form.cleaned_data)
    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        # context['form'] = LoginForm()
        return redirect("/sats")
    else:
         # Return an 'invalid login' error message.
        print("Error")
  return render(request, "auth/login.html", context)


# ----------------------------- register page -------------------------------------
User = get_user_model()
def register_page(request):
  form = RegisterForm(request.POST or None)
  context = {
    'title': 'Registeration page',
    'form': form ,
  }
  if form.is_valid():
    print(form.cleaned_data)
    username = form.cleaned_data.get("username")
    email = form.cleaned_data.get("email")
    password = form.cleaned_data.get("password")
    new_user = User.objects.create_user(username, email, password)
    print(new_user)
  return render(request, "auth/register.html", context)

# ----------------------  lien View -----------------------------------
# --------------------------services page -------------------------

def services_page(request):

  context = {
    'title': 'Services',

  }

  return render(request, 'service/view.html', context )