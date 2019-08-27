from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from testapp.models import *
from testapp.serializers import *

# Create your views here.

class EmployeeDBClassBasedView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated,]

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id',None)
        sal = p_data.get('e_sal',0)
        no = p_data.get('e_no',None)
        print(p_data)
        if id is not None:
            # emp = Employee.objects.get(id=id)
            emp = Employee.objects.filter(e_sal__gte=sal ,e_city='San Jose',e_mobile__startswith='9',e_mobile__endswith='9')
            # emp = Employee.objects.raw("SELECT id,e_no,e_name,e_sal,e_city,e_mobile FROM testapp_employee WHERE id="+str(id)+"")
            serializer = EmployeeSerializer(emp,many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json',status=200)
        qs = Employee.objects.all()
        serializer = EmployeeSerializer(qs, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json',status=200)
