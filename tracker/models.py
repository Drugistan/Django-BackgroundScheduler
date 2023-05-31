from django.db import models
import datetime


# Api Fields


class Covid(models.Model):
    objects = None
    date = models.CharField(max_length=100, default=None, null=True)
    states = models.CharField(max_length=100, null=True)
    positive = models.CharField(max_length=100, null=True)
    negative = models.CharField(max_length=100, null=True)
    pending = models.CharField(max_length=100, null=True)
    hospitalizedCurrently = models.CharField(max_length=100, null=True)
    hospitalizedCumulative = models.CharField(max_length=100, null=True)
    inIcuCurrently = models.CharField(max_length=100, null=True)
    inIcuCumulative = models.CharField(max_length=100, null=True)
    onVentilatorCurrently = models.CharField(max_length=100, null=True)
    onVentilatorCumulative = models.CharField(max_length=100, null=True)
    dateChecked = models.CharField(max_length=100, null=True)
    death = models.CharField(max_length=100, null=True)
    hospitalized = models.CharField(max_length=100, null=True)
    totalTestResults = models.CharField(max_length=100, null=True)
    lastModified = models.CharField(max_length=100, null=True)
    recovered = models.CharField(max_length=100, null=True)
    total = models.IntegerField()
    posNeg = models.IntegerField()
    deathIncrease = models.CharField(max_length=100, null=True)
    hospitalizedIncrease = models.CharField(max_length=100, null=True)
    negativeIncrease = models.CharField(max_length=100, null=True)
    positiveIncrease = models.CharField(max_length=100, null=True)
    totalTestResultsIncrease = models.CharField(max_length=100, null=True)

    # def save(self, *args, **kwargs):
    #     if self.dateChecked.time().strftime('%H:%M:%S') == '24:00:00':
    #         # Set the time to '00:00:00' of the next day
    #         self.dateChecked += datetime.timedelta(days=1)
    #         self.dateChecked = self.my_datetime.replace(hour=0, minute=0, second=0)
    #
    #     if self.lastModified.time().strftime('%H:%M:%S') == '24:00:00':
    #         # Set the time to '00:00:00' of the next day
    #         self.lastModified += datetime.timedelta(days=1)
    #         self.lastModified = self.lastModified.replace(hour=0, minute=0, second=0)
    #
    #     super().save(*args, **kwargs)