from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Student


def index(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'core/index.html', context)

def register(request):
    if request.method == 'POST':
        name = request.POST['username']
        age = request.POST['userage']
        email = request.POST['useremail']
        new_student = Student(name=name, age=age, email=email)
        new_student.save()
        return redirect('index')
    return render(request, 'core/register.html')

def edit(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student': student
    }
    if request.method == 'POST':
        student.name = request.POST['username']
        student.age = request.POST['userage']
        student.email = request.POST['useremail']
        student.save()
        return redirect('index')
        print(user.id)
    return render(request, 'core/edit.html', context)

def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('index')