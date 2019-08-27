import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','restapi1.settings')
django.setup()

from testapp.models import *
from faker import Faker
from random import *
from django.db import connection

faker = Faker()
city_list = ['Bangalore' , 'Chennai','Viathnam','San Jose','Australia','Hyderabad']
graduation_list = ["B.E/B.Tech","M.E/M.Tech","B.Com","M.Com","B.S.C","M.S.C","P.H.D"]
def populate_data(n):
    for count in range(n):
        f_e_no = 'PSI-'+str(randint(1000,3000))
        f_e_name = faker.name()
        f_e_sal = randint(10000,99999)
        f_e_city = choice(city_list)
        f_e_mobile = str(randint(6,9))+get_number()
        emp_record = Employee.objects.get_or_create(e_no = f_e_no, e_name=f_e_name, e_sal=f_e_sal,e_city=f_e_city , e_mobile = f_e_mobile)
    else:
        print('Data Inserted Successfully')
def get_number():
    str_val =''
    for i in range(9):
        str_val+=str(randint(0,9))
    return str_val
# populate_data(20000)
def educationDetails():
    cursor = connection.cursor()
    cursor.execute("SELECT e_no FROM testapp_employee ")
    rows = cursor.fetchall()
    e_ids_list=[]
    for row in rows:
        e_ids_list.append(row[0])
    # print(e_ids_list)

    for count in e_ids_list:
        f_e_no = count
        f_highest_qualification = choice(graduation_list)
        f_temporary_address = faker.city()
        f_permanent_address = faker.city()
        emp_record = Education.objects.get_or_create(e_no = f_e_no
        , highest_qualification=f_highest_qualification
        ,temporary_address=f_temporary_address
        , permanent_address = f_permanent_address)

educationDetails()
