from sys import stderr
from django.shortcuts import render
from django.http import JsonResponse
from . models import *


def index(request):

    return render(request, 'index.html')


def load_students(request):
    students = Student.objects.all()
    data = [{'id': student.id, 'name': student.name, 'email': student.email,
             'passwd': student.passwd, 'phone': student.phone} for student in students]

    return JsonResponse({'data': data})


def add_student(request):

    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    passwd = request.POST['passwd']

    student = Student(name=name, email=email, phone=phone, passwd=passwd)
    student.save()
    data = {'id': student.id, 'name': student.name, 'email': student.email,
            'passwd': student.passwd, 'phone': student.phone}
    return JsonResponse({'status': 'Student Added Succesfully', 'data': data})


def delete_student(request):
    id = request.POST['id']
    student = Student.objects.get(id=id)
    student.delete()
    return JsonResponse({'status': 'Student Deleted Succesfully'})


def update_student(request):

    id = request.POST['id']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    passwd = request.POST['passwd']

    student = Student.objects.get(id=id)
    student.name = name
    student.email = email
    student.phone = phone
    student.passwd = passwd

    student.save()

    return JsonResponse({'status': 'Student Updated Succesfully'})
