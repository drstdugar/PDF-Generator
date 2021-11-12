from django.db import models

# Create your models here.
class MainModel(models.Model):
    fromName = models.CharField(max_length=20)
    fromDesignation = models.CharField(max_length=20)
    toName = models.CharField(max_length=20)
    toDesignation = models.CharField(max_length=20)
    inChargeName = models.CharField(max_length=20)
    inChargeDesignation = models.CharField(max_length=20)
    teamLeadName = models.CharField(max_length=20)
    teamLeadDesignation = models.CharField(max_length=20)
    employeeName = models.CharField(max_length=20)
    employeeDesignation = models.CharField(max_length=20)
    employeeResponsibilities = models.CharField(max_length=100)


    class Meta:
        verbose_name_plural = "Engineers Details"