from django import forms

unit= [
    ('Celsius', 'Celsius'),
    ('Farenheit', 'Farenheit'),
    ]
class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=unit))