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
	course_plan_list = models.course_plan.objects.all()
	return render_to_response('courses.html',{'tabname':'courses', 'course_plan_list': course_plan_list})

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
	tag_list = models.course_tags.objects.all()
	print tag_list
        return render_to_response('onLineCourse.html',{'tabname':'onLineCourse','course_list':course_list, 'tag_list':tag_list})
def bbs(request):
        return render_to_response('bbs.html',{'tabname':'bbs'})
def news(request):
	news_type_dict = {'school_news':[], 'industry_news':[], 'student_news':[]}
	for newsType in news_type_dict.keys():
		newsList = models.news.objects.filter(news_type = newsType)
		news_type_dict[newsType].append(newsList)

	news_list = models.news.objects.all()
	print news_type_dict
        return render_to_response('news.html', {
				  'school_news': models.news.objects.filter(news_type='school_news'), 
				  'industry_news': models.news.objects.filter(news_type='industry_news'), 
				  'student_news': models.news.objects.filter(news_type='student_news'), 
		'news_type_dict':news_type_dict, 'tabname':'news'})
def contact(request):
        return render_to_response('contact.html',{'tabname':'contact'})


