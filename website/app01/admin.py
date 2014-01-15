from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple 
from django.contrib.auth.models import User as djangouser, Group as djangogroup
from django.contrib.sites.models import Site as djangosite
import logging.config, logging, logging.handlers

#admin.site.unregister(djangouser)
#admin.site.unregister(djangogroup)
admin.site.unregister(djangosite)

from models import * 


class NewsAdmin(admin.ModelAdmin):
    #search_fields = ('host','host_status')
    list_display = ('headline','author','publish_date','news_choices','news_type')
class WebUserAdmin(admin.ModelAdmin):
    #search_fields = ('host','host_status')
    pass
class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question', 'display_order')
class NewClassAdmin(admin.ModelAdmin):
        list_display = ('class_name', 'number','start_date','method' )
class GraduateAdmin(admin.ModelAdmin):
        list_display = ('student_name', 'title','company','color' )

class CoursePlanAdmin(admin.ModelAdmin):
	list_display = ('name','brief')
	class Media:
		js = (
		'/static/tinymce/js/tinymce/tinymce.min.js',
		'/static/tinymce/js/tinymce/config.js',

		)
class onLineCourseAdmin(admin.ModelAdmin):
        list_display = ('course_name', 'course_url','description' )

class ClassBriefAdmin(admin.ModelAdmin):
	list_display = ('headline', 'brief')

admin.site.register(course_plan, CoursePlanAdmin)
admin.site.register(class_list)
admin.site.register(course_tags)
admin.site.register(teachers)
admin.site.register(online_course,onLineCourseAdmin)
admin.site.register(graduates,GraduateAdmin)
admin.site.register(new_classes,NewClassAdmin)
admin.site.register(questions,QuestionAdmin)
admin.site.register(news,NewsAdmin)
admin.site.register(signup_info,WebUserAdmin)
admin.site.register(web_user,WebUserAdmin)
