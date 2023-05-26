


import re
from django.shortcuts import render, redirect
from .models import Document, File
from .forms import DocumentForm
from Emp.models import Employee, Department
from django.contrib.auth.decorators import login_required



@login_required
def document_upload(request):
    
    document_types = [1, 2, 3]    
    user = request.user
    try:
        employee = Employee.objects.get(Emp_User=user)
    except Employee.DoesNotExist:
        return redirect('login')

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.Doc_Dept = employee.Emp_Dept
            # form.instance.Doc_Type = request.POST.get('Doc_Type')
            form.save()
            return redirect('/document_upload?success_page=true')
        else:
            print(form.errors)
    else:
        form = DocumentForm()

    return render(request, 'fileupload.html', {'form': form, 'employee': employee, 'document_types': document_types})
