from django import forms

from app.adoption.models import Person, YourRequest

class PersonForm(forms.ModelForm):
	class Meta:
		model=Person

		fields=[
			'first_name',
			'last_name',
			'age',
			'phone',
			'email',
			'address',
		]

		labels={
			'first_name':'First Name:',
			'last_name':'Last Name:',
			'age':'Age:',
			'phone':'Phone:',
			'email':'Email:',
			'address':'Address:',
		}

		widgets={
			'first_name':forms.TextInput(attrs={'class':'form-control', 'autofocus':True}),
			'last_name':forms.TextInput(attrs={'class':'form-control'}),
			'age':forms.TextInput(attrs={'class':'form-control'}),
			'phone':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'address':forms.Textarea(attrs={'class':'form-control'}),
		}

class YourRequestForm(forms.ModelForm):
	class Meta:
		model=YourRequest
		fields=[
			'number_pets',
			'reasons',
		]

		labels={
			'number_pets':'Number of Pets:',
			'reasons':'Reasons to Adoption:',
		}

		widgets={
			'number_pets':forms.TextInput(attrs={'class':'form-control'}),
			'reasons':forms.Textarea(attrs={'class':'form-control'}),
		}