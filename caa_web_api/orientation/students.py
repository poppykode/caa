# import pymysql as py
# from .models import RegNumbers
# from rest_framework.decorators import api_view
# from .serializers import RegNumberSerilizer
# from rest_framework.response import Response
# import json


# @api_view(['GET',])
# def get_reg_numbers(request):
#     if request.method == 'GET':
#         conn = py.connect(host='localhost',user='testing',password='testing',db='students_db')
#         a = conn.cursor()
#         sql = 'SELECT student_number,entry_mode,username FROM reg_numbers'
#         orm = RegNumbers.objects.using('students_db').all()
#         print("ipapa")
#         print(orm)
#         print("end")
#         a.execute(orm)
#         dic={}
#         for student_number,entry_mode,username in a.fetchall():      
#             dic= {
#                 'student_number':student_number,
#                 'entry_mode':entry_mode,
#                 'username':username,
            
#             }
#         print(dic)
#         orm = RegNumbers.objects.raw(sql)
        
#         countrow = a.execute(sql)
#         print(countrow)
#         dataa = a.fetchall()
#         serializer = RegNumberSerilizer(dataa, many=True)
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)