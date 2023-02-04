from django.shortcuts import render
from rest_framework.views import APIView
from . models import User
from . serializers import UserSerializer
from rest_framework.response import Response
# Create your views here.

class UserList(APIView):

    def get(self, request):
        all_data = User.objects.all()
        ser_object = UserSerializer(all_data, many = True)
        return Response(ser_object.data)

class UserSingle(APIView):

    def get(self, request):
        all_data = User.objects.get(email = 'v@gmail.com')
        # Python ==> JSON
        ser_object = UserSerializer(all_data, many = False)
        return Response(ser_object.data)



class UserCreate(APIView):
    
    def post(self, request):
        p_data = request.data
        #JSON ==> Python
        ser_object = UserSerializer(data = p_data)
        if ser_object.is_valid():
            ser_object.save() #iss line pe db mein line create hoga
            return Response(ser_object.data)
        else:
            return Response(ser_object.errors)


class UserPut(APIView):

    def put(self, request, pk):
        row_obj = User.objects.get(id = pk)
        ser_object = UserSerializer(row_obj, data= request.data)
        if ser_object.is_valid():
            ser_object.save()
            return Response(ser_object.data)
        else:
            return Response(ser_object.errors)

        
class UserDelete(APIView):

    def delete(self, request, pk):
        row_obj = User.objects.get(id = pk)
        row_obj.delete()

        all_data = User.objects.all()
        ser_object = UserSerializer(all_data, many = True)
        return Response(ser_object.data)
