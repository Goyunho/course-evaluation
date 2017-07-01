from django.shortcuts import render

from .serializers import *
from rest_framework import viewsets, generics

# Create your views here.
class UniversityAPI(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializers


class UndergraduateAPI(viewsets.ModelViewSet):
    queryset = Undergraduate.objects.all()
    serializer_class = UndergraduateSerializers


class DepartmentAPI(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers


class FacultyAPI(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers


class CourseAPI(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class CourseEvaluationAPI(viewsets.ModelViewSet):
    queryset = CourseEvaluation.objects.all()
    serializer_class = CourseEvaluationSerializers


class EvaluationRecordAPI(viewsets.ModelViewSet):
    queryset = EvaluationRecord.objects.all()
    serializer_class = EvaluationRecordSerializers

