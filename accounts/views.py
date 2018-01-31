from django.shortcuts import render, reverse
from .forms import ProfileForm, UserForm
from django.db import transaction
from django.shortcuts import HttpResponseRedirect





def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
		
			return HttpResponseRedirect(reverse('accounts:login'))
	else:
	    form = UserForm()
	return render(request, 'register.html' ,{'form':form})
	









	