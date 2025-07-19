from importlib.metadata import pass_none

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Admin,Student,Faculty,Course,FacultyCourseMapping
from .forms import AddFacultyForm, AddStudentForm, StudentForm


# from django.http import HttpResponse

# Create your views here.
def adminhome(request):
    auname = request.session["auname"]
    return render(request, "adminhome.html",{"adminuname":auname})
    # return render(request, 'adminhome.html')


def logout(request):
    return redirect("/")

def check_adminlogin(request):
    if request.method == "POST":
        adminuname = request.POST['uname']
        adminpwd = request.POST['pwd']

        flag = Admin.objects.filter(username=adminuname, password=adminpwd)
        print(flag)
        if flag:
            request.session["auname"] = adminuname
            return redirect("adminhome")
            # return render(request,"adminhome.html",{"adminuname":adminuname})
        else:
            messages.error(request, "Login Failed!! Invalid Username or Password")
            # return render(request, "login.html")
            return redirect("login")


def view_students(request):
    students= Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]
    return render(request, "viewstudents.html",{"studentdata":students,"count": count,"adminuname":auname})

def view_faculty(request):
    faculties =Faculty.objects.all()
    count = Faculty.objects.count()
    auname = request.session["auname"]
    return render(request, "viewfaculty.html",{"facultydata":faculties,"count":count,"adminuname":auname})

def view_courses(request):
    courses =Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]
    return render(request, "viewcourses.html", {"coursesdata":courses,"count":count,"adminuname":auname})

def adminstudent(request):
    auname =request.session["auname"]
    return render(request, "adminstudent.html",{"adminuname":auname})

def adminfaculty(request):
    auname = request.session["auname"]
    return render(request, "adminfaculty.html",{"adminuname":auname})

def admincourse(request):
    auname = request.session["auname"]
    return render(request, "admincourse.html",{"adminuname":auname})

def add_course(request):
    auname = request.session["auname"]
    if request.method =="POST":
        dept=request.POST["dept"]
        program=request.POST["program"]
        ay=request.POST["ay"]
        sem=request.POST["sem"]
        year=request.POST["year"]
        ccode=request.POST["ccode"]
        ctitle= request.POST["ctitle"]
        ltps= request.POST["ltps"]
        credits = request.POST["credits"]

        course=Course(
            department=dept,
            program=program,
            academicyear=ay,
            semester=sem,
            year=year,
            coursecode=ccode,
            coursetitle=ctitle,
            ltps =ltps,
            credits =credits

        )
        course.save()
        message= "Course Added successfully!"
        return render(request,"addcourse.html", {"msg":message, "adminuname":auname})

    return render(request,"addcourse.html",{"adminuname":auname})

def updatecourse(request,cid=None):
    auname = request.session["auname"]

    if cid:
        return render(request,"courseupdation.html",{"cid":cid,"adminuname":auname})

    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"updatecourse.html",{"adminuname":auname,"coursesdata":courses, "count":count})

def courseupdated(request):
    auname = request.session["auname"]
    cid = request.POST["cid"]
    ctitle =request.POST["ctitle"]
    ltps = request.POST["ltps"]
    credit = request.POST["credits"]

    Course.objects.filter(id=cid).update(coursetitle=ctitle, ltps=ltps, credits =credit)
    msg= "Course Updated Successfully"
    return render(request,"courseupdation.html",{"adminuname":auname, "msg":msg,"cid":cid})


def deletecourse(request,cid=None):
    auname = request.session["auname"]
    if cid:
        Course.objects.filter(id=cid).delete()
        messages.success(request,f"Course with {cid} ID deleted Successfully!!")
        return redirect("deletecourse")

    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"deletecourse.html",{"coursesdata":courses, "count":count, "adminuname":auname})

def addfaculty(request):
    auname = request.session["auname"]
    form=AddFacultyForm() #non parametarized constructor
    if request.method=="POST":
        form1=AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            messages.success(request, "Faculty added successfully!!")
            return redirect("addfaculty")
            # return HttpResponse("Faculty Added Succesfully")
        else:
            print(form1.errors)
            messages.error(request,"Failed to Add Faculty!!")
            return redirect("addfaculty")
    return render(request, "addfaculty.html",{"form":form, "adminuname":auname})

def delete_faculty(request,fid=None):
    auname = request.session["auname"]
    if fid:
        Faculty.objects.filter(facultyid=fid).delete()
        messages.success(request, f"Faculty with {fid} ID deleted Successfully!!")
        return redirect("delete_faculty")

    faculties= Faculty.objects.all()
    count=Faculty.objects.count()
    return render(request, "deletefaculty.html",{"facultydata":faculties,"count":count, "adminuname":auname})

def add_student(request):
    auname = request.session["auname"]
    form = AddStudentForm()
    if request.method  == "POST":
        form2=AddStudentForm(request.POST)
        if form2.is_valid():
            form2.save()
            messages.success(request,"Student Added Successfully!!")
            return redirect(add_student)
        else:
            print(form2.errors)
            messages.success(request, "Failed to add Student!!")
            return redirect(add_student)
    return render(request,"addstudent.html",{"form":form, "adminuname":auname})

def updatestudent(request, sid=None):
    auname=request.session["auname"]
    if sid:
        student=get_object_or_404(Student,studentid=sid)
        if request.method=="POST":
            form=StudentForm(request.POST,instance=student)
            if form.is_valid():
                form.save()
                return HttpResponse("Student Updated Successfully!!")
            else:
                return HttpResponse("Failed to Update Student Data")
        else:
            form =StudentForm(instance=student)
        return render(request,"studentupdated.html",{"form":form,"adminuname":auname})


    students =Student.objects.all()
    count=Student.objects.count()
    return render(request, "updatestudent.html",{"adminuname":auname,"studentdata":students,"count":count})

def delete_student(request,sid=None):
    auname = request.session["auname"]
    if sid:
        Student.objects.filter(studentid=sid).delete()
        messages.success(request,f"Student with {sid} ID Deleted Successfully!!")
        return redirect(delete_student)
    students= Student.objects.all()
    count =Student.objects.count()
    return render(request,"delete_student.html",{"studentdata":students,"count":count, "adminuname":auname})

def facultycoursemapping(request):
    auname = request.session["auname"]
    fmcourses = FacultyCourseMapping.objects.all()
    count =FacultyCourseMapping.objects.count()

    return render(request,"facultycoursemapping.html",{"adminuname":auname,"fmcourses":fmcourses,"count":count})

def adminchangepwd(request):
    auname = request.session["auname"]
    if request.method =="POST":
        opwd = request.POST["opwd"]
        npwd = request.POST["npwd"]
        flag = Admin.objects.filter(username=auname, password=opwd)
        if flag:
            Admin.objects.filter(username=auname).update(password=npwd)
            msg ="Password Updated Successfully!!"
        else:
            msg ="Password Is Incorrect"
        return render(request,"adminchangepwd.html",{"adminuname":auname, "message":msg})
    return render(request,"adminchangepwd.html",{"adminuname":auname})









