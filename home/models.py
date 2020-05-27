from django.db import models


class FtUser(models.Model):
    user_id = models.CharField(max_length=50)
    real_name = models.CharField(max_length=50)
    tz = models.CharField(max_length=100)

    def __str__(self):
        return self.real_name

    @property
    def activity_periods(self):
        return self.activityperiod_set.all()


class ActivityPeriod(models.Model):
    user = models.ForeignKey('home.FtUser', on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
