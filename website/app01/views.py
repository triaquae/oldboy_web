# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
import models 
import datetime,os,json,time


def index(request):
	class_list = models.course_plan.objects.all()
	return render_to_response('index.html',{'tabname':'homepage', 'class_list': class_list})
def courseDesc(request):
	courseId = request.POST['name']
	getType = request.POST['type']
	if getType == 'brief':
		text = models.course_plan.objects.get(id= courseId).brief
	elif getType == 'header':
		text = models.course_plan.objects.get(id= courseId).headers
	else:
		text = models.course_plan.objects.get(id= courseId).content
	return HttpResponse(text)
def about(request):
	return render_to_response('about.html',{'tabname':'about','teacher_list':models.teachers.objects.all()})

def courses(request):
	try:	
		activeid = int(request.GET['id'])
	except KeyError:
		activeid = 1
	course_plan_list = models.course_plan.objects.all()
	print activeid
	return render_to_response('courses.html',{'tabname':'courses', 'course_plan_list': course_plan_list,'activeid':activeid})


def test(request):
	text = models.course_plan.objects.all()[0].content
	#return render_to_response('text.html', {'text': text})
	return HttpResponse(text)
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
				  'school_news': sorted(models.news.objects.filter(news_type='school_news')), 
				  'industry_news':sorted( models.news.objects.filter(news_type='industry_news')), 
				  'student_news': sorted(models.news.objects.filter(news_type='student_news')), 
		'news_type_dict':news_type_dict, 'tabname':'news'},
		context_instance=RequestContext(request))
def contact(request):
	return render_to_response('contact.html',{'tabname':'contact'})
def signupclass(request):
	class_name = request.POST['className']
	student_Name = request.POST['name']
	educa = request.POST['education']
	phonenum = request.POST['phoneNum']
        msg = request.POST['message']
	text = "ok"
	print "education %s" % educa , msg
	newclass = models.new_classes.objects.get(class_name=class_name)	
	p = models.signup_info(name=student_Name,phone=phonenum,eudcation=educa,classname=newclass,message=msg)
	p.save() 
	return HttpResponse(text)
