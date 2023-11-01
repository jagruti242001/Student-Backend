from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import status
from rest_framework.response import Response
from TestApp.models import Student, Staff , Admin
from TestApp.serializers import StudentMasterSerializer, StaffMasterSerializer, AdminMasterSerializer

# Create your views here.

class AdminLoginView(APIView):
    def post(self, request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")

            kwargs = {}
            if username:
                kwargs["username__iexact"] = username
            if password:
                kwargs["password__iexact"] = password

            data = Admin.objects.filter(**kwargs)
            if data:
                return Response({"success":"login successfull"})
            else:
                return Response({"failed":"Something went wrong"})
        except Exception as ex:
            return Response({"error": str(ex)})

class RegisterStudentView(APIView):
    def post(self, request):
        try:
            data = StudentMasterSerializer(data = request.data)
            if data.is_valid():
                data.save()
                return Response(data.data, status= status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"error": str(ex)})   
        
        
   
class GetStudentsView(APIView):
    def post(self , request):
        try:
            id = request.data.get("id")
            first_name = request.data.get("first_name")
            last_name = request.data.get("last_name")
            date_of_birth = request.data.get("date_of_birth")
            email = request.data.get("email")
            phone_number = request.data.get("phone_number")
            address = request.data.get("address")
            admission_date = request.data.get("admission_date")
            course = request.data.get("course")
            is_approved = request.data.get("is_approved")

            kwargs = {}
            if id:
                kwargs["id"] = id
            if first_name:
                kwargs["first_name"] = first_name
            if last_name:
                kwargs["last_name"] = last_name
            if date_of_birth:
                kwargs["date_of_birth"] = date_of_birth
            if email:
                kwargs["email"] = email
            if phone_number:
                kwargs["phone_number"] = phone_number
            if address:
                kwargs["address"] = address
            if admission_date:
                kwargs["admission_date"] = admission_date
            if course:
                kwargs["course"] = course
            if is_approved:
                kwargs["is_approved"] = is_approved
                
            data = Student.objects.filter(**kwargs)
            serialized_data = StudentMasterSerializer(data, many=True)
            return Response(serialized_data.data)
        except Exception as ex:
            return Response({"error": str(ex)})


class UpdateStudentView(APIView):
    def post(self, request):
        try:
            student_id = request.data.get("id")
            if student_id is None:
                return Response({"error": "Student ID is required"})

            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return Response({"error": "Student not found"})

            serializer = StudentMasterSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response({"error": str(ex)})


class DeleteStudentView(APIView):
    def post(self, request):
        try:
            student_id = request.data.get("id")
            if student_id is None:
                return Response({"error": "Student ID is required"})

            try:
                student = Student.objects.get(id=student_id)
            except Student.DoesNotExist:
                return Response({"error": "Student not found"})

            student.delete()
            return Response({"success": "Student deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response({"error": str(ex)})
