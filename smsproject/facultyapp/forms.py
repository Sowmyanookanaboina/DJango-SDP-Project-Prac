from django import forms

from facultyapp.models import CourseContent


class AddCourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContent
        fields ="__all__"