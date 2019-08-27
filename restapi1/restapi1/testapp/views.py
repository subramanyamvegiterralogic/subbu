from django.shortcuts import render
from testapp.models import *
from testapp.serializers import *
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import View
import io,json
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

@method_decorator(csrf_exempt, name='dispatch')
# @permission_classes((IsAuthenticated,))
# @authentication_classes((BasicAuthentication,))
class EmployeePostPerformsGet(View):
    authentication_classes = [BasicAuthentication,]
    permission_classes = [IsAuthenticated,]

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        p_data = JSONParser().parse(stream)
        id = p_data.get('id',None)
        sal = p_data.get('e_sal',0)
        no = p_data.get('e_no',None)
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


class EmployeeListCreateModelMixin(CreateModelMixin, ListAPIView):
    # queryset = Employee.objects.all()
    queryset = Employee.objects.filter(e_sal__gt=20000)
    serializer_class = EmployeeSerializer
    def post(self,request, *args, **kwargs):
        return self.create(request,*args, **kwargs)

class EmployeeRetriveUpdateDestroyModelMixin(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['GET','POST',])
@permission_classes((IsAuthenticated,))
@authentication_classes((BasicAuthentication,))
def getEmployeeDetails(request,pk):
    try:
        emp = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request=='GET' or request == 'POST':
        serializer = EmployeeSerializer(emp)
        return Response({"msg":"Request Received",'data': request.data})
