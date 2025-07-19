from django.urls import path
from . import views

urlpatterns=[
    path("checkstudentlogin/", views.check_studentlogin, name="check_studentlogin"),
    path("studenthome/",views.studenthome, name="studenthome"),
    path("changepwd/",views.changepwd, name="changepwd"),
    path("updatepwd/", views.changepwd, name="updatepwd"),
    path("studentcourses/",views.studentcourses, name="studentcourses"),
    path("displayscourses/",views.studentcourses, name="displaystudentcourses"),
    path("studentcoursecontent/",views.studentcoursecontent, name="studentcoursecontent")
]