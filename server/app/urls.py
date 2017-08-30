from django.conf.urls import url, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'university', UniversityAPI)
router.register(r'undergraduate', UndergraduateAPI)
router.register(r'department', DepartmentAPI)
router.register(r'faculty', FacultyAPI)
router.register(r'course', CourseAPI)
router.register(r'course-evaluation', CourseEvaluationAPI)
router.register(r'evaluation-record', EvaluationRecordAPI)


urlpatterns = [
    # category
    url(r'^', include(router.urls)),
]
