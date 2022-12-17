from django.db import models


class Quality(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Quality"
        verbose_name_plural = "Qualities"

    def __str__(self):
        return f"{self.name} quality"


class Grade(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Grade"
        verbose_name_plural = "Grades"

    def __str__(self):
        return f"{self.name} grade"


class Operation(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    cost_per_unit = models.FloatField()

    class Meta:
        verbose_name = "Operation"
        verbose_name_plural = "Operations"

    def __str__(self):
        return f"{self.name} operation"


class Material(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    grades = models.ManyToManyField(Grade)
    qualities = models.ManyToManyField(Quality)

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def __str__(self):
        return f"{self.name} material"
