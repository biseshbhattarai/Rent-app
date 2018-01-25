from django import forms  
from .models import Rentapp


class RentAppForm(forms.ModelForm):
	#image = forms.FileField()
	

	class Meta:
		model = Rentapp   
		fields = [
		'location',
		'rooms_available',
		'owner_name',
		'owner_phone_no',
		'image',
		]

