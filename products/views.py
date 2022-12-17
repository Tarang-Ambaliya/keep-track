from django.shortcuts import render

from products.forms import GradeForm, MaterialForm, OperationForm, QualityForm


def quality_form(request):
    if request.method == "POST":
        form = QualityForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QualityForm()
    return render(request, "products.html", {"form": form, "heading": "Quality"})


def grade_form(request):
    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = GradeForm()
    return render(request, "products.html", {"form": form, "heading": "Grade"})


def operation_form(request):
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OperationForm()
    return render(request, "products.html", {"form": form, "heading": "Operation"})


def material_form(request):
    if request.method == "POST":
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MaterialForm()
    return render(request, "products.html", {"form": form, "heading": "Material"})
