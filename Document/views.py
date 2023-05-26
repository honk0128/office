import re
from django.shortcuts import render, redirect
from .models import Document, File
from .forms import DocumentForm
from Emp.models import Employee, Department

def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            document = Document()
            user = Employee.objects.get(Emp_User = request.user)
            document.Doc_ID = 1
            document.Doc_Dept = user.Emp_Dept
            document.Doc_Sender = request.POST.get('Doc_Sender')
            document.Doc_Receiver = request.POST.get('Doc_Receiver')
            document.Doc_Title = request.POST.get('Doc_Title')
            document.Doc_Type = request.POST.get('Doc_Type')
            document.Doc_State = 2
            document.save()
            return redirect('/document_upload?success_page=true')
        else:
            print(form.errors) 
    else:
        form = DocumentForm()
    return render(request, 'fileupload.html', {'form': form})
