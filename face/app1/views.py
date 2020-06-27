from django.shortcuts import render
from random import randint


def index(request):
	# a=randint(1,5)
	# a="/"+str(a)+".jpg"

	# args={"a":a}
	return render(request,'home.html')