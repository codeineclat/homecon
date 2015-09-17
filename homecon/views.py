from django.shortcuts import render

def index(request):
	posts = "bye"
	return render(request,"homecon/index.html",{'posts': posts})