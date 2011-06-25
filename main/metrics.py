

def healthMetrics(healthInput):
	
	if healthInput < 10:
		healthSmoker = 10
		healthFat = 10
		healthGood = 0
	elif healthInput >= 10 and healthInput <= 30:
		healthSmoker = 5
		healthFat = 8
		healthGood = 2
	elif healthInput >= 30 and healthInput <= 60:
		healthSmoker = 5
		healthFat = 5
		healthGood = 5
	elif healthInput > 60:
		healthSmoker = 0
		healthFat = 0
		healthGood = 10
		
	return { 'healthSmoker': healthSmoker, 'healthFat' : healthFat, 'healthGood' : healthGood }

def foodMetrics(foodInput):
	
	if foodInput < 1:
		foodStandsCount = 0
		foodStandsAvailable = False
		marketAvailable = False
		marketWithProduce = False
	elif foodInput >= 1 and foodInput < 5:
		foodStandsCount = 0
		foodStandsAvailable = False
		marketAvailable = True
		marketWithProduce = False
	elif foodInput >= 5:
		foodStandsCount = int(round ((foodInput - 5) / 10))
		if foodStandsCount > 0:
			foodStandsAvailable = True
		marketAvailable = True
		marketWithProduce = True
		
	return { 'marketAvailable' : marketAvailable, 'marketWithProduce' : marketWithProduce, 'foodStandsAvailable' : foodStandsAvailable, 'foodStandsCount': foodStandsCount }


def infraMetrics(infraInput):
	
	if infraInput < 5:
		# Grass
		roadType = 1
	elif infraInput >= 5 and infraInput < 7:
		# Roads
		roadType = 2
	elif infraInput >= 7 and infraInput < 10:
		# Bus service
		roadType = 3
	elif infraInput >= 10:
		# Metro
		roadType = 4
	
	return {'roadType' : roadType}

def envMetrics(envInput):
	
	if envInput < 1:
		bushesAvailable = True
		treesCount = 0
	elif envInput >=1 and envInput < 2:
		bushesAvailable = False
		treesAvailable = True
		treesCount = 1
	elif envInput >=2 and envInput < 10:
		bushesAvailable = False
		treesAvailable = True
		treesCount = int(envInput)
	elif envInput >= 10:
		bushesAvailable = False
		treesAvailable = False
		parkAvailable = True
		treesCount = 0
		
	return { 'bushesAvailable' : bushesAvailable, 'treesAvailable' : treesAvailable, 'treesCount' : treesCount, 'parkAvailable' : parkAvailable }


def safetyMetrics(safetyInput):
	
	peopleCount = 0
	gangCount = 0
	policeAvailable = False
	
	if safetyInput < 3:
		peopleCount = 0
		gangCount = 3
	elif safetyInput >= 3 and safetyInput < 8:
		peopleCount = 10
		gangCount = 3
	elif safetyInput >=8 and safetyInput < 28:
		if gangCount > 0:
			gangCount = gangCount - int(round ((safetyInput - 8) / 5))
	elif safetyInput >= 28:
		policeAvailable = True
		gangCount = 0
		
	return { 'peopleCount' : peopleCount, 'gangCount' : gangCount, 'policeAvailable' : policeAvailable }

def govMetrics(govInput):
	
	multiplier = 0
	libraryAvailable = False
	fireworksAvailable = False
	
	if govInput > 0 and govInput < 5:
		multiplier = 0.66
	elif govInput >=5 and govInput < 50:
		multiplier = 2
	elif govInput >= 50 and govInput < 75:
		libraryAvailable = True
	elif govInput >= 75:
		libraryAvailable = True
		fireworksAvailable = True
		
	return { 'multiplier' : multiplier, 'libraryAvailable' : libraryAvailable, 'fireworksAvailable' : fireworksAvailable }

def higherEduMetrics(higherEduInput):
	
	if higherEduInput < 33:
		businessLevel = 1
	elif higherEduInput >= 33 and higherEduInput < 66:
		businessLevel = 2
	elif higherEduInput >= 66:
		businessLevel = 3
		
	return {'businessLevel' : businessLevel}

def k12EduMetrics(k12EdInput):
	
	if k12EdInput < 20:
		pass
	elif k12EdInput >=20 and k12EdInput < 40:
		schoolAvailable = True
		sportsTeamAvailbale = False
		scienceFairAvailable = False
		artsAndMusicAvailable = False
		awesomeGradRatesAvailable = False
	elif k12EdInput >= 40 and k12EdInput < 60:
		schoolAvailable = True
		sportsTeamAvailbale = True
		scienceFairAvailable = False
		artsAndMusicAvailable = False
		awesomeGradRatesAvailable = False	
	elif k12EdInput >= 60 and k12EdInput < 80:
		schoolAvailable = True
		sportsTeamAvailbale = False
		scienceFairAvailable = True
		artsAndMusicAvailable = False
		awesomeGradRatesAvailable = False
	elif k12EdInput >= 80 and k12EdInput < 100:
		schoolAvailable = True
		sportsTeamAvailbale = False
		scienceFairAvailable = False
		artsAndMusicAvailable = True
		awesomeGradRatesAvailable = False
	elif k12EdInput == 100:
		schoolAvailable = True
		sportsTeamAvailbale = False
		scienceFairAvailable = False
		artsAndMusicAvailable = False
		awesomeGradRatesAvailable = True
		
	return { 'schoolAvailable' : schoolAvailable, 
			'sportsTeamAvailbale' : sportsTeamAvailbale, 
			'scienceFairAvailable' : scienceFairAvailable, 
			'artsAndMusicAvailable' : artsAndMusicAvailable, 
			'awesomeGradRatesAvailable' :  awesomeGradRatesAvailable
			}


