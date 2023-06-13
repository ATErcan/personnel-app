from django.db import models

class Department(models.Model):
  department_name = models.CharField(max_length=100)
  
  def __str__(self):
    return self.department_name
  


class Personnel(models.Model):
  
  GENDER = (
    (1, 'Female'),
    (2, 'Male'),
    (3, 'Other')
  )
  
  TITLE = (
    (1, 'Junior'),
    (2, 'Mid'),
    (3, 'Senior'),
    (4, 'Team Lead')
  )
  
  department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='department')
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  gender = models.SmallIntegerField(choices=GENDER)
  salary = models.IntegerField()
  is_staff = models.BooleanField(default=False)
  title = models.SmallIntegerField(choices=TITLE)
  join_date = models.DateField(auto_now_add=True)
