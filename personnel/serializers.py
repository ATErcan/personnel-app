from rest_framework import serializers
from .models import Department, Personnel


class PersonnelSerializer(serializers.ModelSerializer):
  department_id = serializers.IntegerField()
  department = serializers.StringRelatedField()
  
  class Meta:
    model = Personnel
    fields = (
      'id',
      'department_id',
      'department',
      'first_name',
      'last_name',
      'gender',
      'salary',
      'is_staff',
      'title',
    )


class DepartmentSerializer(serializers.ModelSerializer):
  personnel = PersonnelSerializer(many=True, read_only=True, source='department')
  
  class Meta:
    model = Department
    fields = (
      'id',
      'department_name',
      'personnel'
    )
