# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import datetime,os,json,time


def index(request):

	return render_to_response('index.html')


def courses(request):
	return render_to_response('courses.html')

def graduate(request):
        return render_to_response('graduate.html')
                                                 
def enroll(request):
	return render_to_response('enroll.html') 

def onLineCourse(request):
        return render_to_response('onLineCourse.html')
def bbs(request):
        return render_to_response('bbs.html')
def news(request):
        return render_to_response('news.html')
def contact(request):
        return render_to_response('contact.html')

