from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect



# Home Page
def main(request):
	return render(request, "main_templates/home.html")