from django.shortcuts import render

from .serializers import *
from rest_framework import viewsets, generics
from rest_framework.response import Response

# Create your views here.
class UniversityAPI(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializers

    def list(self, requests):
        queryset = University.objects.all()
        serializer_context = {'request': requests}
        serializer = UniversityListSerializers(queryset, many=True, context=serializer_context)
        return Response(serializer.data)


class UndergraduateAPI(viewsets.ModelViewSet):
    queryset = Undergraduate.objects.all()
    serializer_class = UndergraduateSerializers

    def list(self, requests):
        queryset = Undergraduate.objects.all()
        serializer_context = {'request': requests}
        serializer = UndergraduateListSerializers(queryset, many=True, context=serializer_context)
        return Response(serializer.data)


class DepartmentAPI(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

    def list(self, requests):
        queryset = Department.objects.all()
        serializer_context = {'request': requests}
        serializer = DepartmentListSerializers(queryset, many=True, context=serializer_context)
        return Response(serializer.data)


class FacultyAPI(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers


class CourseAPI(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    # def list(self, requests):
    #     queryset = Course.objects.all()
    #     serializer_context = {'request': requests}
    #     serializer = CourseListSerializers(queryset, many=True, context=serializer_context)
    #     return Response(serializer.data)


class CourseEvaluationAPI(viewsets.ModelViewSet):
    queryset = CourseEvaluation.objects.all()
    serializer_class = CourseEvaluationSerializers


class EvaluationRecordAPI(viewsets.ModelViewSet):
    queryset = EvaluationRecord.objects.all()
    serializer_class = EvaluationRecordSerializers

