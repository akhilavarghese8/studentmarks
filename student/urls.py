from django.urls import path
from .views import AddStudentView,ListStudentsView



urlpatterns = [
    path('add/students/', AddStudentView.as_view(), name='add_students'),
    path('list/students/', ListStudentsView.as_view(), name='list_students'),
]

