
from django.urls import path

from . import views

urlpatterns=[
    path("check_facultylogin/",views.check_facultylogin, name="check_facultylogin"),
    path("facultyhome/",views.facultyhome, name ="facultyhome"),
    path("myfcourses/", views.facultycourses, name="facultycourses"),
    path("facultychangepwd/",views.facultychangepwd, name="facultychangepwd"),
    path("facultyupdatepwd/",views.facultychangepwd, name="facultyupdatepwd"),
    path("facultycoursecontent/", views.facultycoursecontent, name="facultycoursecontent"),
]