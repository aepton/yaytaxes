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
  tweets = [
             {'user': 'brainzzz',
              'tweet_text': 'Hey, look, zombies!'},
             {'user': 'Suzie',
              'tweet_text': "Hey, guys, the water alert's been lifted! We can drink the water from the tap again!"},
             {'user': 'new2CA',
              'tweet_text': "I don't even know why I bothered making an online appointment for the DMV. I'm going to stand in line for three and a half hours either way."},
             {'user': 'bibliophile',
              'tweet_text': 'There is a new library branch LESS than a mile from my house!! This could be dangerous...'},
             {'user': 'hermanmunster',
              'tweet_text': "The Museum of Science and Industry's new Harry Potter exhibit is AWESOME!"},
             {'user': 'proud_one',
              'tweet_text': 'The pride parade was EPIC this year! So happy to see how the city supports the LBGT folks!'},
             {'user': 'redbirdmom',
              'tweet_text': 'just heard about the bridge collapse. sending prayers to my SF friends'},
             {'user': 'storm',
              'tweet_text': 'Man, you never realize how everything you use requires power until it goes out for 12 hours.'},
             {'user': '7thgradeboy',
              'tweet_text': 'Learned about typhoid Mary today...think that could happen here?'},
             {'user': 'vroom',
              'tweet_text': 'Finally fixed that pothole on Fillmore! Was worried about shocks for a while.'},
             {'user': 'Govgeek',
              'tweet_text': 'Resolution to require CFLs passed! Typical CFLs consume 4x less energy, and last 8x longer than the usual incandescent light bulbs.'},
             {'user': 'disgruntled',
              'tweet_text': 'New bus line one block from my house, goes 3 blocks from work! Huzzah no more horrible commute!'},
             {'user': 'prtygrl',
              'tweet_text': "2 am is drunken sea shanty time on MUNI! So glad I didn't have to drive tonight."},
             {'user': 'weezie',
              'tweet_text': 'The air is brown today. No going outside for me!'},
             {'user': 'hungry',
              'tweet_text': "Turns out it's true, you can fry an egg on the sidewalk!"},
             {'user': 'whysitsohot',
              'tweet_text': 'A tree grows in Brooklyn, but not in my town. :('},
             {'user': 'Environerd',
              'tweet_text': 'Plastic bag ban passed! Sorry, Kevin Spacey.'},
             {'user': 'pastorlibby',
              'tweet_text': 'The whole neighborhood turned out for the ceremonial planting of the tree in the park. http://www.flickr.com/photos/mountauburncemetery/3470992499/'},
             {'user': 'fadedblond',
              'tweet_text': 'Awesome to eat veggies grown from soil using my compost bin!'},
             {'user': 'greentshirt',
              'tweet_text': 'Fire on 33rd and Main still out of control. The whole block has been evacuated.'},
             {'user': '33trees',
              'tweet_text': 'frack! someone stole my bike'},
             {'user': 'rocketgrl',
              'tweet_text': "Fewer gangs than last year, but still don't wear black and red below 16th st. "},
             {'user': 'doctorspooky',
              'tweet_text': 'Average police response time in city down to less than 15 minutes! Lowest crime rates in 25 years.'},
             {'user': 'pocahontas',
              'tweet_text': 'I might have to move since the new fire station opened -- sirens and horns ALL NIGHT LONG!'},
             {'user': 'happyharry',
              'tweet_text': 'Kids walked to school by themselves for the first time today. Bittersweet moment!'},
             {'user': 'mumto3',
              'tweet_text': "Small boy has an hour long bus ride to middle school this year. He's too tired to learn, but what do you do?"},
             {'user': 'boycalledmuffin',
              'tweet_text': 'Got an 87 on my math test. Stupid algebra, when am I going to use this in real life?'},
             {'user': 'Goofy',
              'tweet_text': 'Watching basketball tryouts. Some guys seem unfamiliar with concept of bright orange balls that bounce.'},
             {'user': 'physicsjen',
              'tweet_text': 'Asked to judge first science fair at the middle school -- and only three baking soda and vinegar volcanos!'},
             {'user': 'theycallmemimi',
              'tweet_text': 'Maria flubbed lines, abbey walls fell down, Capt. Von Trapp might have the flu. This production is cursed.'},
             {'user': 'classof2011',
              'tweet_text': 'Graduation today! Awesome to read in the program about all the colleges my class is attending!'},
             {'user': 'tacoslave',
              'tweet_text': 'fed up with my boss. looking for a new gig, but so far nothing.'},
             {'user': 'greenteen',
              'tweet_text': 'finished that damn FAFSA. hope the pell grant comes through.'},
             {'user': 'thisaway',
              'tweet_text': 'aced my chem final! 1 down, 3 to go.'},
             {'user': 'labrrrat',
              'tweet_text': 'team at UC running trials on new cancer vaccine!'},
             {'user': 'artmajor',
              'tweet_text': 'I GOT MY SCHOLARSHIP!! No loans for me!'},
             {'user': 'goldbear2012',
              'tweet_text': "just landed a summer job with google"},
             {'user': 'twofish',
              'tweet_text': "staying inside with the kids today. not taking any risks with the whooping cough outbreak in Marin."},
             {'user': 'jockrock97',
              'tweet_text': "Still at the ER. Five hours and counting, and my ankle still hurts like hell."},
             {'user': 'marylouwho',
              'tweet_text': "My gramma has cancer. :( Fifth person on this block!"},
             {'user': 'skinnymaker',
              'tweet_text': "Weigh-in today! I've lost 15 lbs since the beginning of the month! Wish I could get the hubby to join me."},
             {'user': 'runathenarun',
              'tweet_text': "logged a 6.0 mile run on Saturday, June 25!"},
             {'user': 'stayinalive',
              'tweet_text': "Everyone in SF now eligible for Healthy San Francisco! Now no one has to choose between rent and the doctor."},
             {'user': 'oakladee',
              'tweet_text': "I'll hella miss Oakland! Hello Omaha."},
             {'user': 'kindersam',
              'tweet_text': "looking for a roommate, need to downsize. ah, the glamorous life of a preschool teacher."},
             {'user': 'uphillbothways',
              'tweet_text': "I paid more than $15k in taxes this year and there's still a pothole the size of Oakland on Main St. So frustrating!"},
             {'user': 'fatcat',
              'tweet_text': "How is it possible that I make $250k and can't afford to live in San Francisco? Something's wrong here."},
           ] 
  index = random.randint(0, len(tweets) - 1)
  return HttpResponse(json.dumps(tweets[index]))    
  # All the following is nice but not ready in time
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