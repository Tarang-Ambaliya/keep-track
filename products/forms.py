from django import forms

from products.models import Grade, Material, Operation, Quality


class QualityForm(forms.ModelForm):
    class Meta:
        model = Quality
        fields = ["name", "description"]
        labels = {"name": "Name", "description": "Description"}


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["name", "description"]
        labels = {"name": "Name", "description": "Description"}


class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ["name", "description"]
        labels = {"name": "Name", "description": "Description"}


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            "name",
            "description",
            "grades",
            "qualities",
        ]
        labels = {
            "name": "Name",
            "description": "Description",
            "grades": "Grades",
            "qualities": "Qualities",
        }
