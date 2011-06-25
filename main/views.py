from django.template import Context, loader
from django.http import HttpResponse
from main.models import HouseholdIncome

def index(request):
	t = loader.get_template('main/index.html')
	c = Context()
	return HttpResponse(t.render(c))
	
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
