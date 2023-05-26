from django import forms
from .models import Document, File

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['Doc_ID', 'Doc_Dept','Doc_Title', 'Doc_Sender', 'Doc_Receiver',  'Doc_Type', 'Doc_State', 'Doc_Content']
