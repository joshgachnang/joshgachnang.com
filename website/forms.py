from django import forms

class ContactForm(forms.Form):
    sender = forms.CharField()
    sender_email = forms.EmailField(label="Email")
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)