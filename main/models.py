from django.db import models

class HouseholdIncome(models.Model):
	income = models.IntegerField()
	households = models.IntegerField()
	
	def __unicode__(self): return '%s (%s) (%s)' % (self.id, self.income, self.households)

class Tweets(models.Model):
  user = models.CharField(max_length=50)
  tweet_text = models.CharField(max_length=140)
  service = models.CharField(max_length=50)
  budget_amount = models.IntegerField()
  
  def __unicode__(self): return '%s (%s) (%s) (%s) (%s)' % (self.id,
                                                            self.user,
                                                            self.tweet_text,
                                                            self.service,
                                                            self.budget_amount)
  
class HoodAttributes(models.Model):
  attributes = models.TextField()
  
  def __unicode__(self): return '%s (%s)' % (self.id, self.attributes)