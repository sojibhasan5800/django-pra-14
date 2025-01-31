from django import forms
from .models import muscian_model,album_model

class user_muscian_from(forms.ModelForm):
    class Meta:
        model = muscian_model
        fields = '__all__'

     


class user_album_from(forms.ModelForm):
    class Meta:
        model = album_model
        fields = '__all__'
        widgets={
             'rating': forms.Select(attrs={'class': 'form-control'}),
        }
     





        

