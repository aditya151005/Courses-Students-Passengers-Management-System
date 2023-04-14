from rest_framework import serializers
from cbvCourseapp.models import Course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['name','description','ratings']