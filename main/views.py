from django.template import Context, loader
from django.http import HttpResponse
from main.models import HouseholdIncome
import json

def index(request):
	t = loader.get_template('main/index.html')
	c = Context()
	return HttpResponse(t.render(c))

def tweets(request):
  user_id = request.GET.get('id', '')
  if not user_id:
    print 'No ID provided'
    return HttpResponse('No ID provided', status=500)
    
  # First, get all decisions made by user
  
  # Next, get all relevant tweets for those decisions
  
  # Finally, decide which to display
  # Importantly, don't want to display the same one twice consecutively
  
  response_obj = {'tweet_text': 'I am a tweet', 'user': 'aepton'}
  return HttpResponse(json.dumps(response_obj))
	
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