from django.db import models
from django.contrib.auth.models import User

class Ticket (models.Model):
    user = models.ForeignKey (User)
    case_number = models.IntegerField(null=True)
    username=models.TextField(null=True)
    dollar_amount = models.DecimalField('Cost (in dollars)', max_digits=10, decimal_places=2,null=True)

    def __unicode__(self):
        return u"%s" % self.id