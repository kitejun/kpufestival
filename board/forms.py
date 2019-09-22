from django import forms
from .models import Board, Missing

class BoardPost(forms.ModelForm):
        class Meta:
            model = Board
            fields = ['title','context','image']
            widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'context': forms.Textarea(attrs={'class': 'form-control'}),
            }

class MissingPost(forms.ModelForm):
        class Meta:
            model = Missing
            fields = ['context','image']
            widgets = {
                'context': forms.Textarea(attrs={'class': 'form-control'}),
            }