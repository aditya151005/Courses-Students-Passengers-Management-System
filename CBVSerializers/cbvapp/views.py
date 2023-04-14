from django.shortcuts import render
from django.shortcuts import render
from cbvapp.models import Student
from cbvapp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404 
from rest_framework import generics,mixins
from rest_framework import viewsets

#using ViewSet
class StudentViewSet(viewsets.ModelViewSet):
      queryset=Student.objects.all()
      serializer_class=StudentSerializer





#using generics
# class StudentList(generics.ListCreateAPIView):
#         queryset=Student.objects.all()
#         serializer_class=StudentSerializer
# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#       queryset=Student.objects.all()
#       serializer_class=StudentSerializer


#using mixins
# for non-primary key based operations
# class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self,request):
#         return self.list(request)
#     def post(self,request):
#         return self.create(request)
# for primary key based operations
# class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self,request,pk):
#         return self.update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)

 
#class Based view approach

# Create your views here.
#for non-primary key based operations
# class StudentList(APIView):
    
#     def get(self,request):
#         students=Student.objects.all()
#         serializer=StudentSerializer(students,many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#for primary key based operations
# class StudentDetail(APIView):
    
#     def get_object(self,pk):
#         try:
#             return Student.objects.get(pk=pk)
#         except Student.DoesNotExist:
#             return Http404
        
#     def get(sellf,request,pk):
#         student=sellf.get_object(pk)
#         serializer=StudentSerializer(student)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         student=self.get_object(pk)
#         serializer=StudentSerializer(student,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         student=self.get_object(pk)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    