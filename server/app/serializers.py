from rest_framework import serializers
from .models import *


# Course
class CourseSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


# Department
class DepartmentListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class DepartmentSerializers(serializers.HyperlinkedModelSerializer):
    course = CourseSerializers(many=True, read_only=True)
    class Meta:
        model = Department
        fields = ('id', 'url', 'name', 'course')


# Undergraduate
class UndergraduateListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Undergraduate
        fields = '__all__'


class UndergraduateSerializers(serializers.HyperlinkedModelSerializer):
    department = DepartmentListSerializers(many=True, read_only=True)
    class Meta:
        model = Undergraduate
        fields = ('id', 'url', 'name', 'department')


# University
class UniversityListSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class UniversitySerializers(serializers.HyperlinkedModelSerializer):
    undergraduate = UndergraduateListSerializers(many=True, read_only=True)
    class Meta:
        model = University
        fields = ('id', 'url', 'name', 'name_short', 'name_en', 'name_en_short', 'undergraduate', )


# Faculty
class FacultySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class CourseEvaluationSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CourseEvaluation
        fields = '__all__'


class EvaluationRecordSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EvaluationRecord
        fields = '__all__'
