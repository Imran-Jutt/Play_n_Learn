from django.db import models


class signUp(models.Model):
    U_Name = models.CharField(max_length=30)
    U_Email = models.CharField(max_length=30)
    U_Password = models.CharField(max_length=30)
    U_id = models.AutoField(primary_key=True)

    def __str__(self):
        return '%s' % self.U_Name