from django import forms

class MyForm(forms.Form):
    department = forms.ChoiceField(choices=[('sc','Select department'),('cs', 'Computer Science'), ('ece', 'Electronics'), ('commerce', 'Commerce'), ('humanities', 'Humanities'), ('math', 'Mathematics')])
    course = forms.ChoiceField(choices=[])

