from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class web_user(models.Model):
    user = models.ForeignKey(User, null=True)
    email = models.EmailField()
    photo = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return '%s' % self.user

class news(models.Model):
	headline = models.CharField(max_length=100, unique=True)
	author = models.CharField(max_length=30)
	publish_date = models.DateTimeField()
	news_choices = (('school_news','school news'), ('industry_news', 'industry news'), ('student_news','student news'))
        news_type = models.CharField(max_length=100, choices= news_choices)
	
	content = models.TextField()	
        def __unicode__(self):
        	return self.headline
class questions(models.Model):
	question =  models.CharField(max_length=150, unique=True)
	answer =  models.TextField()
	display_order = models.IntegerField(default=1000)
	def __unicode__(self):
                return self.question
class online_course(models.Model):
	course_name = models.CharField(max_length=100, unique=True)
	description = models.CharField(max_length=100, unique=True)
	course_url = models.URLField()
	img_link = models.CharField(max_length=100, unique=True)
	display_order = models.IntegerField(default=1000)
class new_classes(models.Model):
	class_name = models.CharField(max_length=100, unique=True)
	number = models.CharField(max_length=30)
	start_date = models.DateField()
	course_term = models.CharField(max_length=30)
	method =  models.CharField(max_length=30)
	students = models.CharField(max_length=30)
	limited = models.BooleanField(default=False,verbose_name='Seat limited')
	def __unicode__(self):
                return self.number


class graduates(models.Model):
	student_name = models.CharField(max_length=30, unique=True)
	photo = models.CharField(max_length=100)
	title = models.CharField(max_length=30)
	company = models.CharField(max_length=50, unique=True)
	comments = models.TextField()	
	color_choice = (('br-orange','orange'), ('br-green', 'green'), ('br-blue','blue'),('br-red','red'),('br-lblue','light-blue'),('br-black',('black')))
        color = models.CharField(max_length=100, choices= color_choice)
'''
class IP(models.Model):
    hostname=models.CharField(max_length=50, unique=True)
    ip = models.IPAddressField(unique=True)
    group = models.ManyToManyField(Group, null=True, blank=True)
    port = models.IntegerField(default='22')
    os = models.CharField(max_length=20, default='linux', verbose_name='Operating System')

    #snmp related
    alert_limit = models.IntegerField(default=5)
    snmp_alert_limit = models.IntegerField(default=5)
    asset_collection = models.BooleanField(default=True,verbose_name='enable asset collection')
    status_monitor_on = models.BooleanField(default=True)
    snmp_on = models.BooleanField(default=True)
    snmp_version = models.CharField(max_length=10,default='2c')
    snmp_community_name = models.CharField(max_length=50,default='public')
    snmp_security_level = models.CharField(max_length=50,default='auth')
    snmp_auth_protocol = models.CharField(max_length=50,default='MD5')
    snmp_user = models.CharField(max_length=50,default='triaquae_snmp')
    snmp_pass = models.CharField(max_length=50,default='my_pass')
    system_load_warning = models.IntegerField(default=0,blank=True,verbose_name="load >")
    system_load_critical = models.IntegerField(default=0,blank=True)
    cpu_idle_warning = models.IntegerField(default=0,blank=True, verbose_name = "cpuIdle% < ")
    cpu_idle_critical= models.IntegerField(default=0,blank=True)
    mem_usage_warning = models.IntegerField(default=0,blank=True, verbose_name="memoryUsage% >")

'''
