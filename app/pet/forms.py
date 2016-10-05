from django import forms

from app.pet.models import Pet

class PetForm(forms.ModelForm):
	class Meta:
		model=Pet

		fields=[
			'name',
			'sex',
			'age_approx',
			'date_recovery',
			'person',
			'vaccine',
		]

		labels={
			'name':'Name:',
			'sex':'Sex:',
			'age_approx':'Age(approx):',
			'date_recovery':'Date of Recovery:',
			'person':'Adopter:',
			'vaccine':'Vaccines:',
		}

		widgets={
			'name':forms.TextInput(attrs={'class':'form-control', 'autofocus':True}),
			'sex':forms.TextInput(attrs={'class':'form-control'}),
			'age_approx':forms.TextInput(attrs={'class':'form-control'}),
			'date_recovery':forms.TextInput(attrs={'class':'form-control'}),
			'person':forms.Select(attrs={'class':'form-control'}),
			'vaccine':forms.CheckboxSelectMultiple(),
		}