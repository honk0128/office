import re
from django.shortcuts import render, redirect
from .models import Document, File
from .forms import DocumentForm
from Emp.models import Employee, Department




def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.Doc_Dept = Employee.objects.get(Emp_User = request.user).Emp_Dept
            form.save()
            return redirect('/document_upload?success_page=true')
        else:
            print(form.errors) 
    else:
        form = DocumentForm()
    return render(request, 'fileupload.html', {'form': form, 'user': request.user})
