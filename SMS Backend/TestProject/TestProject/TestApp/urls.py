from django.urls import path
from .views import GetStudentsView,AdminLoginView,UpdateStudentView,RegisterStudentView,DeleteStudentView

urlpatterns = [
    path("get_students/", GetStudentsView.as_view(), name = 'get_specific_user'),
    path("admin_login/", AdminLoginView.as_view(), name = 'admin_login'),
    path("register_student/", RegisterStudentView.as_view(), name = 'register_student'),
    path("update_student/", UpdateStudentView.as_view(), name = 'update_student'),
    path("delete_student/", DeleteStudentView.as_view(), name = 'delete_student'),
]