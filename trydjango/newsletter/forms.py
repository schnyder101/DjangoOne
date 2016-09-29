from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	class Meta:
		model=SignUp
		fields=['email','full_name']

	#Custom validator below for email:	#access other fields like clean_xyz
	# def clean_email(self):
	# 	email= self.cleaned_data.get('email')
	# 	email_base,provider = email.split('@')
	# 	domain,extension= provider.split('.')
		
	# 	if not extension=="edu":
	# 		raise forms.ValidationError("Please use a .edu email address")
	# 	return email
	def clean_FullName(self):
		full_name=self.cleaned_data.get('full_name')
		return full_name
# # Custom form example below
class ContactForm(forms.Form):
	full_name=forms.CharField(required=False)
	email=forms.EmailField()
	message=forms.CharField()
	