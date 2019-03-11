from django import forms



class contactus(forms.Form):
	your_name = forms.CharField(
		label='',
		widget = forms.TextInput(
			attrs ={
			"placeholder": "Your Name",
			"class": "form-control",
			"id": "name",
			"name": "name",
			})
		)
	email = forms.EmailField(
		label='',
		widget = forms.TextInput(
			attrs ={
			"placeholder": "Your email",
			"class": "form-control",
			"id": "youremail",
			"name": "youremail",
			})
		)
	subject = forms.CharField(
		label='',
		widget = forms.TextInput(
			attrs ={
			"placeholder": "Subject",
			"class": "form-control",
			"id": "subject",
			"name": "subject",
			})
		)
	message = forms.CharField(
		label='',
		widget = forms.Textarea(
			attrs = {
			"placeholder": "Message",
			"class": "form-control",
			'cols': '20',
			'rows': '4',
			"id": "message",
			"name": "message",
			"maxlength": "100",
			}
			)
		)