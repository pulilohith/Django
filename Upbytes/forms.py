from django import forms
from Upbytes.models import Employee


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class StudForm(forms.Form):
    FirstName = forms.CharField(label="Enter the first Name", max_length=50)
    LastName = forms.CharField(label="Enter the last Name", max_length=50)
    file_upload = forms.FileField()
