from django import forms
import datetime

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class contact_from(forms.Form):
    name = forms.CharField(max_length=23)
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'comment1'}))
    value = forms.DecimalField(required=False,label="values",initial=10)
    day = forms.DateField(initial= datetime.date.today)
    favourit= forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    more_fave = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)