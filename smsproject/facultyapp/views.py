from django.shortcuts import render,redirect
from django.contrib import messages

from adminapp.models import Faculty,Course, FacultyCourseMapping

from facultyapp.forms import AddCourseContentForm


# Create your views here.
def check_facultylogin(request):
    if request.method == "POST":
        fid = request.POST["fid"]
        pwd = request.POST["pwd"]
        flag = Faculty.objects.filter(facultyid=fid, password=pwd)
        print(flag)
        if flag:
            request.session["fid"] =fid
            messages.success(request,"Login Successful")
            return redirect("facultyhome")
        else:
            messages.error(request,"Login Failed!!Invalid ID Or Password")
            return redirect("facultylogin")

def facultyhome(request):
    fid = request.session["fid"]
    return render(request,"facultyhome.html",{"fid":fid})

def facultycourses(request):
    fid = request.session["fid"]
    # courses = Course.objects.all()
    # count = Course.objects.count()
    mappingcourses = FacultyCourseMapping.objects.all()
    fmcourses =[]
    # print(mappingcourses)
    for course in mappingcourses:
        # print(course.faculty.facultyid)
        if (course.faculty.facultyid == int(fid)):
            fmcourses.append(course)
    print(fmcourses)
    count = len(fmcourses)
    return render(request,"facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})

def facultychangepwd(request):
    fid = request.session["fid"]
    if request.method=="POST":
        opwd = request.POST["opwd"]
        npwd= request.POST["npwd"]
        flag=Faculty.objects.filter(facultyid=fid,password=opwd)
        if flag:
            Faculty.objects.filter(facultyid=fid).update(password=npwd)
            msg ="Password Updated Successfully"
        else:
            msg="Old Password in Incorrect"
        return render(request,"facultychangepwd.html",{"fid":fid,"message":msg})
    return render(request, "facultychangepwd.html",{"fid":fid})

def facultycoursecontent(request):
    form = AddCourseContentForm()
    if request.method =="POST":
        form1=AddCourseContentForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            messages.success(request,"Course Content Added Succefully")
            return redirect("facultycoursecontent")
        else:
            print(form1.errors)
            messages.error(request,"Unable to add Course Content")
            return redirect("facultycoursecontent")

    return render(request,"facultycoursecontent.html",{"form":form})