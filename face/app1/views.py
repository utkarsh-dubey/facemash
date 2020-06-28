from django.shortcuts import render
from random import randint


def index(request):
	
	
	a = randint(1, 94)
	b = randint(1, 94)
	print(a)
	while a==b:
		b - randint(1, 56)
	filepath = "/static/"+str(a)+".jpg"
	filepath2 = "/static/"+str(b)+".jpg"
	args = {
		"a":filepath,
		"b":filepath2
	}
	winner =''
	loser=''
	if 'first' in request.POST:
		winner='first'
		winner_number=request.POST['first']
		winner_number=winner_number[winner_number.index('c')+2:winner_number.index('.')]
		loser='second'
	elif 'second' in request.POST:
		winner='second'
		winner_number=request.POST['second']
		winner_number=winner_number[winner_number.index('c')+2:winner_number.index('.')]
		loser='first'

		
	return render(request,'home.html',args)