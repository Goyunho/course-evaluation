from rest_framework import serializers
from .models import *

class UniversitySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class UndergraduateSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Undergraduate
        fields = '__all__'


class DepartmentSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class FacultySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class CourseSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseEvaluationSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseEvaluation
        fields = '__all__'


class EvaluationRecordSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EvaluationRecord
        fields = '__all__'
