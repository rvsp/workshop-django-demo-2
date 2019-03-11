
from django.contrib.auth import get_user_model
from django.db.models import Q

from django import forms

User = get_user_model()

class UserCreationForm(forms.ModelForm):
	firstname = forms.CharField(
		label='', 
		widget=forms.TextInput(attrs ={
                        "placeholder" : "First Name",
                        "class" : "form-control mb-3"
                        }))
	lastname = forms.CharField(
		label='', 
		widget=forms.TextInput(attrs ={
                        "placeholder" : "Last Name",
                        "class" : "form-control mb-3"
                        }))

	username = forms.CharField(
		label='', 
		widget=forms.TextInput(attrs ={
                        "placeholder" : "Username",
                        "class" : "form-control mb-3"
                        }))

	email = forms.EmailField(
		label='', 
		widget=forms.TextInput(attrs ={
                        "placeholder" : "E-Mail",
                        "class" : "form-control mb-3"
                        }))

	password1 = forms.CharField(
		label='', 
		widget=forms.PasswordInput(attrs ={
                        "placeholder" : "Password",
                        "class" : "form-control mb-3"
                        }))
	password2 = forms.CharField(
		label='', 
		widget=forms.PasswordInput(attrs ={
                        "placeholder" : "Conform Password",
                        "class" : "form-control mb-3"
                        }))
	mobile = forms.CharField(
		label = '',
		widget = forms.TextInput(attrs = {
			"placeholder" : "Mobile No",
			"class" : "form-control mb-3"
		}))
	branch = forms.CharField(
		label = '',
		widget = forms.TextInput(attrs = {
			"placeholder" : "Branch",
			"class" : "form-control mb-3"
		}))
	class Meta:
		model = User
		fields = ['firstname','lastname','username', 'email','branch','mobile','is_superuser']

	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords do not match")
		return password2

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


class UserLoginForm(forms.Form):

	query = forms.CharField(label='',widget=forms.TextInput(attrs ={
                        "placeholder": "Username",
                        "class": "form-control"
                        }))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs ={
                        "placeholder": "Password",
                        "class": "form-control"
                        }))

	def clean(self, *args, **kwargs):
		query = self.cleaned_data.get('query')
		password = self.cleaned_data.get('password')
		user_qs_final = User.objects.filter(
				Q(username__iexact=query)
			).distinct()
		
		if not user_qs_final.exists() and user_qs_final.count != 1:
			raise forms.ValidationError("Invalid credentials - user does note exist")
		user_obj = user_qs_final.first()
		if not user_obj.check_password(password):
			raise forms.ValidationError("credentials are not correct")
		self.cleaned_data["user_obj"] = user_obj
		return super(UserLoginForm, self).clean(*args, **kwargs)
		



