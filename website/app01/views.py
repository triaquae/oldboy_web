# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import models 
import datetime,os,json,time


def index(request):

	return render_to_response('index.html',{'tabname':'homepage'})
def about(request):
	return render_to_response('about.html',{'tabname':'about','teacher_list':models.teachers.objects.all()})

def courses(request):
	return render_to_response('courses.html',{'tabname':'courses'})

def graduate(request):
	student_list = models.graduates.objects.all()
        return render_to_response('graduate.html',{'student_list':student_list,'tabname':'graduate'})
                                                 
def enroll(request):
	question_list = models.questions.objects.all()
	return render_to_response('enroll.html',{'question_list': sorted(question_list) ,'tabname':'enroll'}) 

def newClass(request):
	new_classes = models.new_classes.objects.all()
	return render_to_response('newClass.html', {'new_classes': new_classes,'tabname':'newClass'})
def onLineCourse(request):
	course_list = models.online_course.objects.all()
        return render_to_response('onLineCourse.html',{'course_list':course_list})
def bbs(request):
        return render_to_response('bbs.html',{'tabname':'bbs'})
def news(request):
	news_list = models.news.objects.all()
        return render_to_response('news.html', {'news_list': news_list,'tabname':'news'})
def contact(request):
        return render_to_response('contact.html',{'tabname':'contact'})


