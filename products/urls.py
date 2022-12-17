from django.urls import path

from products import views


urlpatterns = [
    path("quality/", views.quality_form, name="quality form"),
    path("grade/", views.grade_form, name="grade form"),
    path("operation/", views.operation_form, name="operation form"),
    path("material/", views.material_form, name="material form"),
]
