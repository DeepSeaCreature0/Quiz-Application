from django import forms
from .models import Response

class ResponseForm(forms.ModelForm):
    CHOICES = (
        ('Cricket', 'Cricket'),
        ('Football', 'Football'),
        ('BasketBall', 'BasketBall'),
        ('Soccer', 'Soccer'),
    )

    favorite_game = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Response
        fields = ['favorite_game']
