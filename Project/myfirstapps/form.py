from django import forms
class Feedback(forms.Form):
    title=forms.CharField(label='Title',max_length=50,widget=forms.TextInput(attrs={'class:form-control'}))
    subject=forms.CharField(label='Subject',max_length=150,widget=forms.Textarea(attrs={'class:form-control'}))