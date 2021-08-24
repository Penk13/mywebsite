from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Full Name'})
    )
    email = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Email', 'type': 'email'})
    )
    message = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5})
    )
