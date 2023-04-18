

# Create your views here.


from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from student.models import Student
from student.forms import StudentForm

class AddStudentView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add_student.html'
    success_url = reverse_lazy('add_students')
class ListStudentsView(ListView):
    model = Student
    template_name = 'list_student.html'
    context_object_name="student"
    
