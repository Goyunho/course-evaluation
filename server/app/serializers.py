from rest_framework import serializers
from .models import *


class UndergraduateSerializers(serializers.HyperlinkedModelSerializer):
    department = serializers.StringRelatedField(many=True)
    class Meta:
        model = Undergraduate
        fields = ('id', 'url', 'name', 'department')
        # fields = '__all__'


class UniversitySerializers(serializers.HyperlinkedModelSerializer):
    # undergraduate = serializers.StringRelatedField(many=True)
    undergraduate = UndergraduateSerializers(many=True, read_only=True)
    class Meta:
        model = University
        fields = ('id', 'url', 'name', 'name_short', 'name_en', 'name_en_short', 'undergraduate', )
        # fields = '__all__'


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
