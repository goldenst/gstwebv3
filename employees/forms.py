from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):
  class Meta:
    model = Employee
    fields = [
      'aaaDriverNumber',
      'firstName',
      'lastName',
      'address',
      'city',
      'state',
      'zipCode',        
      'email',
      'driversLicence',
      'dlExpire',
      'cellphone',
      'homePhone',
      'hiredate',
      'emergencyContact',
      'emerContactPhone',
      'emerContactRelation',
      'isDriver',
      'isDispatcher',
      'isManager',
      'termDate',
      'notes'
    ]
    