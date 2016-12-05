from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from myblog import models

def archive(request):
	posts = models.BlogPost.objects.all()
	t = loader.get_template("archive.html")
	c = Context({'posts':posts})
	return HttpResponse(t.render(c))

# Create your views here.
