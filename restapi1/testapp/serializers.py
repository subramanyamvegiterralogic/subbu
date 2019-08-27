from rest_framework.serializers import ModelSerializer
from testapp.models import Employee

# Create your serializers here.

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
