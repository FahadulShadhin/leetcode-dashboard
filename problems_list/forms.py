from django import forms
from django.forms import ModelForm
from .models import Problem

class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = (
            'name', 
            'topic', 
            'difficulty', 
            'link', 
            'note', 
            'source_code'
        )
