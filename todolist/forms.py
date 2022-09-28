from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label="Judul", max_length=100)
    description = forms.CharField(label="Deskripsi", max_length=250)