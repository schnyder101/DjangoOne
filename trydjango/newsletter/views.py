from django.shortcuts import render
from .forms import SignUpForm,ContactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):
	title="Subscribe below"
	form =SignUpForm(request.POST or None)
	if request.user.is_authenticated():
		title='My Title %s' %(request.user)
		form =SignUpForm(request.POST or None)
		
		if form.is_valid():
			#form.save()
			print "bbbbbb"
			instance=form.save(commit=False)
			name=form.cleaned_data.get('full_name')
			if not name:
				name="Kenshin"
				print name
			instance.full_name=name
			instance.save()
	context ={
		"template_title": title,
		"form":form,
	}
	return render(request,"home.html",context)


#view for custom contact form
def contact(request):
	
	form=ContactForm(request.POST or None)
	title='Contact Us'
	title_align_center=True
	context={
			"form":form,
			"title":title,
			"title_align_center":title_align_center,
		}
	if form.is_valid():
		
		message=form.cleaned_data.get('message')
		name=form.cleaned_data.get('full_name')

		send_mail(
		    'Contact Form for:',
		    message,
		    settings.EMAIL_HOST_USER,
		    ['suharsh18@gmail.com'],
		    fail_silently=False,
			)
	return render(request,"forms.html",context)