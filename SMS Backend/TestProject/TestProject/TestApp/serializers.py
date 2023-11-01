from TestApp.models import Student, Staff, Admin
from rest_framework import serializers

class StudentMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class StaffMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
        
class AdminMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"