from django.shortcuts import render
import io,json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.db import connection
# Create your views here.

common_dict={}
@api_view(['GET',])
def return_data(request):
    emp_data={
        'e_no'  :   'PSI-1931',
        'e_name':   'Subramanyam.V',
        'e_city':   'Bangalore'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data, content_type='application/json')

@api_view(['POST',])
def create_new_record(request):
    json_req = request.body
    stream_data = io.BytesIO(json_req)
    req_data = JSONParser().parse(stream_data)
    eno = req_data.get('e_no',None)
    ename = req_data.get('e_name',None)
    esal = req_data.get('e_sal',None)
    ecity = req_data.get('e_city',None)
    emobile = req_data.get('e_mobile',None)
    print(len(eno))
    if eno is None or len(eno)<1:
        common_dict['status_code']='404'
        common_dict['status_message']='eno is Mandatory'
        json_data = JSONRenderer().render(common_dict)
        return HttpResponse(json_data, content_type='application/json',status=404)
    else:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM testapp_employee WHERE e_no='"+eno+"'")
        count = cursor.fetchone()
        print(count)
        if count is None:
            cursor.execute("INSERT INTO testapp_employee (e_no,e_name,e_sal,e_mobile,e_city) VALUES ('"+eno+"','"+ename+"','"+esal+"','"+emobile+"','"+ecity+"')")
            print('No Records Found')
            common_dict['status_message']='Record Inserted Successfully'
        else:
            cursor.execute("UPDATE testapp_employee SET e_no='"+eno+"',e_name='"+ename+"',e_sal='"+str(esal)+"',e_mobile='"+emobile+"',e_city='"+ecity+"' WHERE e_no='"+eno+"'")
            print('Records Found')
            common_dict['status_message']='Record Updated Successfully'
        common_dict['status_code']='200'
        json_data = JSONRenderer().render(common_dict)
        return HttpResponse(json_data, content_type='application/json',status=404)


@api_view(['POST','GET',])
def get_data(request):
    local_db_list = []
    json_data = request.body
    stream = io.BytesIO(json_data)
    p_data = JSONParser().parse(stream)
    city = p_data.get('e_city',None)
    eno = p_data.get('e_no',None)
    esal = p_data.get('e_sal',None)
    # print(p_data)

    if city is None or len(city)<1 or eno is None or len(eno)<1:
        common_dict['status_code']='400'
        common_dict['status_message']='Invalid Input'
        common_dict['data']=local_db_list
        json_data = JSONRenderer().render(common_dict)
        return HttpResponse(json_data,content_type='application/json',status=400)
    else:
        cursor = connection.cursor()
        # cursor.execute("SELECT em.e_no,em.e_name,em.e_sal,em.e_mobile,em.e_city,ed.highest_qualification,ed.temporary_address,ed.permanent_address FROM testapp_employee as em JOIN testapp_education as ed ON em.e_no=ed.e_no WHERE em.e_sal>"+esal+" AND em.e_city LIKE '"+city+"%' ORDER BY em.e_no DESC")
        cursor.execute("SELECT em.e_no,em.e_name,em.e_sal,em.e_mobile,em.e_city,ed.highest_qualification,ed.temporary_address,ed.permanent_address FROM testapp_employee as em JOIN testapp_education as ed ON em.e_no=ed.e_no ORDER BY em.e_name ASC")
        rows = cursor.fetchall()
        # print(rows)
        if len(rows) != 0 or len(rows) is not None:
            common_dict['status_code']='200'
            common_dict['status_message']='Data sent Successfully'
            common_dict['session_key']=get_session_id_from_db()
            for row in rows:
                db_data ={}
                db_data['e_no'] = row[0]
                db_data['e_name'] = row[1]
                db_data['e_sal'] = row[2]
                db_data['e_mobile'] = row[3]
                db_data['e_city'] = row[4]
                db_data['highest_qualification'] = row[5]
                db_data['temporary_address'] = row[6]
                db_data['permanent_address'] = row[7]
                local_db_list.append(db_data)
            common_dict['data']=local_db_list
        json_data = JSONRenderer().render(common_dict)
        return HttpResponse(json_data,content_type='application/json',status=200)

def get_session_id_from_db():
    cursor = connection.cursor()
    cursor.execute("SELECT session_key FROM django_session ORDER BY session_key DESC")
    session_key = cursor.fetchone()
    return session_key[0]


@api_view(['PUT',])
def put_details(request):
    json_req = request.body
    stream_data = io.StringIO(json_req)
    req_data = JSONParser().parse(stream_data)
    eno = req_data.get('e_no',None)
    if eno is None:
        common_dict['status_code']='404'
        common_dict['status_message']='eno is Mandatory'
        json_data = JSONRenderer().render(common_dict)
        return HttpResponse(json_data, content_type='application/json',status_code=404)

@api_view(['PATCH',])
def patch_details(request):
    json_req = request.body
    stream_data = io.StringIO(json_req)
    req_data = JSONParser().parse(stream_data)
    eno = req_data.get('e_no',None)
    if eno is None:
        common_dict['status_code']='404'
        common_dict['status_message']='eno is Mandatory'
        json_data = JSONRenderer().render(common_dict)
        return HttpResponse(json_data, content_type='application/json',status_code=404)

@api_view(['DELETE',])
def delete_details(request,pk):
    json_req = request.body
    stream_data = io.StringIO(json_req)
    req_data = JSONParser().parse(stream_data)
    eno = req_data.get('e_no',None)
    # if eno is None:
    common_dict['status_code']='404'
    common_dict['status_message']='eno is Mandatory'
    json_data = JSONRenderer().render(common_dict)
    return HttpResponse(json_data, content_type='application/json',status_code=404)
