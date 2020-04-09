from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


# ---------------------------- Contact form -----------------------------------
class ContactForm(forms.Form):
  fullname    = forms.CharField(
              widget=forms.TextInput(
                  attrs={
                    "class": "form-control", 
                    "placeholder": "Name"
                    }
                    )
              )
  email       = forms.EmailField(
              widget=forms.EmailInput(
                  attrs={
                    "class": "form-control", 
                    "placeholder": "Email"
                    }
                    )
              )
  message     = forms.CharField(
              widget=forms.Textarea(
                  attrs={
                    "class": "form-control", 
                    "placeholder": "My Message"
                    }
                    )
              )

# ---------------------------- Login form -----------------------------------

class LoginForm(forms.Form):
  username  = forms.CharField(
              widget=forms.TextInput(
                  attrs={
                    "class": "form-control", 
                    "placeholder": "Userame"
                    }
                    )
              )
  password  = forms.CharField(
              widget=forms.PasswordInput(
                  attrs={
                    "class": "form-control", 
                    "Plalceholder": "Password"
                    }
                    )
              )


# ---------------------------- Register  form -----------------------------------
class RegisterForm(forms.Form):
  username  = forms.CharField()
  email  = forms.CharField()
  password  = forms.CharField(widget=forms.PasswordInput)
  password2  = forms.CharField(label="Confirm Password" , widget=forms.PasswordInput)

  def clean_username(self):
    username = self.cleaned_data.get('username')
    qs = User.objects.filter(username=username)
    if qs.exists():
      raise forms.ValidationError('UserName is Taken')
    return username

  def clean_email(self):
    email = self.cleaned_data.get('email')
    qs = User.objects.filter(email=email)
    if qs.exists():
      raise forms.ValidationError('email is Taken')
    return email

  def clean(self):
    data = self.cleaned_data
    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')
    if password2 != password:
      raise forms.ValidationError('passwords must match')
    return data



# ------------------ job app -------------------------

class job_applicationForm(forms.Form):
  firstName   = forms.CharField()
  lastName    = forms.CharField()
  email       = forms.EmailField()
