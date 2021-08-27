from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Add Comment Here ..'}),
    )
