from django import forms
from .models import Board, Missing

class BoardPost(forms.ModelForm):
        class Meta:
            model = Board
            fields = ['title','context','image']

class MissingPost(forms.ModelForm):
        class Meta:
            model = Missing
            fields = ['context','image']