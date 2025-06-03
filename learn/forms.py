from django import forms
from django.forms import ModelForm
from .models import Feedback, ContactModel


class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'email': forms.EmailInput(),
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    # Custom clean method
    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@gmail.com'):
            raise forms.ValidationError("Only Gmail is allowed.")
        return email


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'feedback']
        Widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'form-control'}),
            'feedback': forms.Textarea(attrs={'rows': 5}),
        }
