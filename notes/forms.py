from django import forms
from notes.models import Note


class NoteForm(forms.ModelForm):
    content = forms.Textarea()

    class Meta:
        model = Note
        fields = ["content"]
