from django import forms


class StudentForm(forms.Form):
    matric_no = forms.CharField(label='Matriculation Number', max_length=20)
    name = forms.CharField(label='Name', max_length=100)
    semester1_grades = forms.CharField(label='Semester 1 Grades', max_length=100)
    semester1_course_units = forms.CharField(label='Semester 1 Course Units', max_length=100)
    semester2_grades = forms.CharField(label='Semester 2 Grades', max_length=100)
    semester2_course_units = forms.CharField(label='Semester 2 Course Units', max_length=100)
