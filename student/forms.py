from django import forms
from student.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'date_of_birth', 'physics_marks', 'chemistry_marks', 'maths_marks', 'computer_science_marks']