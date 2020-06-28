from django.shortcuts import render
from random import randint


def index(request):
	
	winner ='nope'
	loser=''
	if 'first' in request.POST:
		winner='first'
		loser='second'
	elif 'second' in request.POST:
		winner='second'
		loser='first'

	print(winner)
	print(loser)
	a = randint(1, 94)
	b = randint(1, 94)
	while a==b:
		b - randint(1, 56)
	filepath = "/static/"+str(a)+".jpg"
	filepath2 = "/static/"+str(b)+".jpg"
	args = {
		"a":filepath,
		"b":filepath2
	}
	return render(request,'home.html',args)