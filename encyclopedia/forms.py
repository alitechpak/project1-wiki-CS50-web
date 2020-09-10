from django import forms


class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={"placeholder":"Title"}))
    NewPage = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': "Enter you content here..."}))

