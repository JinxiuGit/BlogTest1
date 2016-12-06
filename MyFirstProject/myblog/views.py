from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from myblog import models

def homePage(request):
	posts = models.BlogPost.objects.all()
	t = loader.get_template("homePage.html")
	c = Context({'author':'firmworm','posts':posts})
	return HttpResponse(t.render(c))

def aboutMe(request):
	t = loader.get_template("aboutMe.html") 
	c = Context()
	return HttpResponse(t.render(c))

def blogDisplay(request,id_num):
	post = models.BlogPost.objects.get(id = id_num)
	t = loader.get_template("blogDisplay.html")
	#c = Context({'id_num':id_num,'posts':posts})
	c = Context({'post':post})
	return HttpResponse(t.render(c))

