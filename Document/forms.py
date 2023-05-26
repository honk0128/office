from django import forms
from .models import Document, File

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['Doc_ID', 'Doc_Dept', 'Doc_Sender', 'Doc_Receiver', 'Doc_Title', 'Doc_Type', 'Doc_State']
