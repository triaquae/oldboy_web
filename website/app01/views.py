# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import models 
import datetime,os,json,time


def index(request):

	return render_to_response('index.html')
def about(request):
	return render_to_response('about.html')

def courses(request):
	return render_to_response('courses.html')

def graduate(request):
        return render_to_response('graduate.html')
                                                 
def enroll(request):
	question_list = models.questions.objects.all()
	return render_to_response('enroll.html',{'question_list': sorted(question_list) }) 

def newClass(request):
	new_classes = models.new_classes.objects.all()
	return render_to_response('newClass.html', {'new_classes': new_classes})
def onLineCourse(request):
        return render_to_response('onLineCourse.html')
def bbs(request):
        return render_to_response('bbs.html')
def news(request):
	news_list = models.news.objects.all()
        return render_to_response('news.html', {'news_list': news_list})
def contact(request):
        return render_to_response('contact.html')


