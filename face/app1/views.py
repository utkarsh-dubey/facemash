from django.shortcuts import render
from random import randint


def index(request):
	
	a = randint(1, 56)
	b = randint(1, 56)
	while a==b:
		b - randint(1, 56)
	filepath = "/static/"+str(a)+".jpg"
	filepath2 = "/static/"+str(b)+".jpg"
	args = {
		"a":filepath,
		"b":filepath2
	}
	return render(request,'home.html',args)