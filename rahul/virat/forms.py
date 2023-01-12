from django import forms
from django.contrib.auth.models import User
from virat.models import UserProfileInfo
# from virat.models import User

# class FormName(forms.Form):
# 	name = forms.CharField()
# 	email = forms.EmailField()
# 	text = forms.CharField(widget=forms.Textarea)


# class NewUser(forms.ModelForm):
# 	class Meta():
# 		model = User
# 		fields = '__all__'

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta():
		model = User
		fields = ('username','email','password')
class ProfileInfo(forms.ModelForm):
	class Meta():
		model = UserProfileInfo
		fields = ('portfolio_site','profile_pic')
