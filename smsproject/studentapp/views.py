from django.shortcuts import render, redirect
from django.contrib import messages
from adminapp.models import Student,Course

from facultyapp.models import CourseContent


# Create your views here.
def studenthome(request):
    sid = request.session["sid"]
    student = Student.objects.get(studentid=sid)
    return render(request, "studenthome.html",{"sid":sid,"student":student})



def check_studentlogin(request):
    if request.method == "POST":
        sid = request.POST['sid']
        pwd = request.POST['pwd']

        flag = Student.objects.filter(studentid=sid, password=pwd)
        print(flag)
        if flag:
            request.session["sid"] = sid
            return redirect("studenthome")
            # return render(request,"studenthome.html",{"sid":sid})
        else:
            messages.error(request, "Login Failed!! Invalid Username or Password")
            # return render(request, "login.html")
            return redirect("studentlogin")

def changepwd(request):
    sid = request.session["sid"]
    if request.method=="POST":
        opwd=request.POST["opwd"]
        npwd =request.POST["npwd"]
        flag=Student.objects.filter(studentid=sid,password=opwd)
        if flag:
            Student.objects.filter(studentid=sid).update(password=npwd)
            msg="Password Updated Successfully"
        else:
            msg="Old Password is Incorrect"
        return render(request,"studentchangepwd.html",{"sid":sid,"message":msg})
    return render(request,"studentchangepwd.html",{"sid":sid})

def studentcourses(request):
    sid = request.session["sid"]
    if request.method =="POST":
        ay = request.POST["ay"]
        sem =request.POST["sem"]
        courses= Course.objects.filter(academicyear=ay, semester=sem)
        return render(request,"displaystudentcourses.html",{"courses":courses,"sid":sid})
    return render(request,"studentcourses.html",{"sid":sid})

def studentcoursecontent(request):
    sid =request.session["sid"]
    content =CourseContent.objects.all()
    return render(request, "studentcoursecontent.html",{"sid":sid,"coursecontent":content})