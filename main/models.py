from django.db import models

class HouseholdIncome(models.Model):
	income = models.IntegerField()
	households = models.IntegerField()
	
	def __unicode__(self): return '%s (%s) (%s)' % (self.id, self.income, self.households)

