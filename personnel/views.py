from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import DepartmentSerializer, PersonnelSerializer
from .models import Department, Personnel
from .permissions import IsStaffOrAddOnly

class DepartmentView(ModelViewSet):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer
  permission_classes = [IsAuthenticated]


class PersonnelView(ModelViewSet):
  queryset = Personnel.objects.all()
  serializer_class = PersonnelSerializer
  permission_classes = [IsStaffOrAddOnly, IsAuthenticated]