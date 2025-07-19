"""
URL configuration for smsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .import views

urlpatterns = [
    path("adminhome/", views.adminhome, name="adminhome"),
    path('adminlogout/',views.logout,name="logout"),
    path("checkadminlogin/", views.check_adminlogin, name="check_adminlogin"),

    path("adminstudent/",views.adminstudent, name="adminstudent"),
    path("add_student/",views.add_student,name="add_student"),
    path("viewstudents/",views.view_students, name="view_students"),
    path("deletestudent/",views.delete_student,name="delete_student"),
    path("deletestudent/<int:sid>",views.delete_student, name ="studentdeletion"),
    path("updatestudent/",views.updatestudent, name="updatestudent"),
    path("studentupdation/<int:sid>", views.updatestudent, name="studentupdation"),



    path("adminfaculty/", views.adminfaculty, name="adminfaculty"),
    path("viewfaculty/",views.view_faculty, name="view_faculty"),
    path("addfaculty/",views.addfaculty,name="addfaculty"),
    path("delete_faculty/",views.delete_faculty, name="delete_faculty"),
    path("delete_faculty/<int:fid>",views.delete_faculty,name="faculty_deletion"),
    path("updatefaculty", views.updatefaculty, name="updatefaculty"),
    path("facultyupdated/<int:fid>", views.updatefaculty, name="facultyupdated"),


    path("veiwcourse/", views.view_courses, name="view_courses"),
    path("admincourse/",views.admincourse, name="admincourse"),
    path("add_course/",views.add_course, name="add_course"),
    path("updatecourse/",views.updatecourse,name="updatecourse"),
    path("courseupdation/<int:cid>",views.updatecourse,name="courseupdation"),
    path("courseupdated/",views.courseupdated,name="courseupdated"),

    path("deletecourse/",views.deletecourse, name="deletecourse"),
    path("deletecourse/<int:cid>",views.deletecourse, name="coursedeletion"),

    path("facultycoursemapping/",views.facultycoursemapping,name="facultycoursemapping"),
    path("adminchangepwd/",views.adminchangepwd,name="adminchangepwd"),
    path("adminupdatepwd/",views.adminchangepwd,name= "adminupdatepwd"),




]