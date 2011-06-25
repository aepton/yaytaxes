from django.template import Context, loader
from django.http import HttpResponse
from main.models import HouseholdIncome
from main.models import HoodAttributes
from main.models import Tweets
from metrics import *
import json
import random

def index(request):
	t = loader.get_template('main/index.html')
	c = Context()
	return HttpResponse(t.render(c))
	
def scale(raw):
  return 20 * int(round(float(raw)/float(20)))

def tweets(request):
  user_id = request.GET.get('id', '')
  if not user_id:
    print 'No ID provided'
    return HttpResponse('No ID provided', status=500)
  
  # First, get all user neighborhood attributes
  neighborhood = json.loads(HoodAttributes.objects.get(id=user_id).attributes)
  print 'Atts: %s' % neighborhood

  # Next, get all relevant tweets for those decisions
  dimensions = ['environment', 'government', 'infrastructure', 'safety', 'k-12',
                'higher ed']
  candidates = []
  for d in dimensions:
    tweets = Tweets.objects.filter(budget_amount=scale(neighborhood[d]),
                                   service=d)
    for tweet in tweets:
      candidates.append({'tweet_text': tweet.tweet_text, 'user': tweet.user})
    
  # Finally, decide which to display
  index = random.randint(0, len(candidates) - 1)
  return HttpResponse(json.dumps(candidates[index]))
	
def yaytaxesland(request):
	t = loader.get_template('main/yaytaxesland.html')
	c = Context()
	return HttpResponse(t.render(c))	
	
def incomes(request):
	household_incomes = HouseholdIncome.objects.all()
	t = loader.get_template('main/incomes.html')
	c = Context({
		'household_incomes': household_incomes,
	})
	return HttpResponse(t.render(c))

def metrics(request):
	totalDict = dict( healthMetrics(int(request.GET['health'])).items() + foodMetrics(int(request.GET['food'])).items() + infraMetrics(int(request.GET['infra'])).items() + envMetrics(int(request.GET['env'])).items() + safetyMetrics(int(request.GET['safety'])).items() + govMetrics(int(request.GET['gov'])).items() + higherEduMetrics(int(request.GET['edu'])).items() + k12EduMetrics(int(request.GET['k12'])).items() )
	
	t = loader.get_template('main/metrics.html')
	c = Context({
		'totalDict' : json.dumps(totalDict),
	})
	return HttpResponse(t.render(c))