# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'web_user'
        db.create_table(u'app01_web_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('class_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app01.class_list'])),
            ('photo', self.gf('django.db.models.fields.CharField')(default='user-1.jpg', max_length=100)),
        ))
        db.send_create_signal(u'app01', ['web_user'])

        # Adding model 'news'
        db.create_table(u'app01_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app01.web_user'])),
            ('publish_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('news_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'app01', ['news'])

        # Adding model 'questions'
        db.create_table(u'app01_questions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(default=1000)),
        ))
        db.send_create_signal(u'app01', ['questions'])

        # Adding model 'course_plan'
        db.create_table(u'app01_course_plan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('headers', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(default=1000)),
        ))
        db.send_create_signal(u'app01', ['course_plan'])

        # Adding model 'teachers'
        db.create_table(u'app01_teachers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('photo', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('social_blog_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('social_blog_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('introduction', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'app01', ['teachers'])

        # Adding model 'course_tags'
        db.create_table(u'app01_course_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'app01', ['course_tags'])

        # Adding model 'online_course'
        db.create_table(u'app01_online_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('course_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('course_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('img_link', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('display_order', self.gf('django.db.models.fields.IntegerField')(default=1000)),
        ))
        db.send_create_signal(u'app01', ['online_course'])

        # Adding M2M table for field tag_name on 'online_course'
        m2m_table_name = db.shorten_name(u'app01_online_course_tag_name')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('online_course', models.ForeignKey(orm[u'app01.online_course'], null=False)),
            ('course_tags', models.ForeignKey(orm[u'app01.course_tags'], null=False))
        ))
        db.create_unique(m2m_table_name, ['online_course_id', 'course_tags_id'])

        # Adding model 'new_classes'
        db.create_table(u'app01_new_classes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('class_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('course_term', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('students', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('limited', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app01', ['new_classes'])

        # Adding model 'graduates'
        db.create_table(u'app01_graduates', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('student_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('photo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('class_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app01', ['graduates'])

        # Adding model 'class_list'
        db.create_table(u'app01_class_list', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'app01', ['class_list'])


    def backwards(self, orm):
        # Deleting model 'web_user'
        db.delete_table(u'app01_web_user')

        # Deleting model 'news'
        db.delete_table(u'app01_news')

        # Deleting model 'questions'
        db.delete_table(u'app01_questions')

        # Deleting model 'course_plan'
        db.delete_table(u'app01_course_plan')

        # Deleting model 'teachers'
        db.delete_table(u'app01_teachers')

        # Deleting model 'course_tags'
        db.delete_table(u'app01_course_tags')

        # Deleting model 'online_course'
        db.delete_table(u'app01_online_course')

        # Removing M2M table for field tag_name on 'online_course'
        db.delete_table(db.shorten_name(u'app01_online_course_tag_name'))

        # Deleting model 'new_classes'
        db.delete_table(u'app01_new_classes')

        # Deleting model 'graduates'
        db.delete_table(u'app01_graduates')

        # Deleting model 'class_list'
        db.delete_table(u'app01_class_list')


    models = {
        u'app01.class_list': {
            'Meta': {'object_name': 'class_list'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'app01.course_plan': {
            'Meta': {'object_name': 'course_plan'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'headers': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'app01.course_tags': {
            'Meta': {'object_name': 'course_tags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'app01.graduates': {
            'Meta': {'object_name': 'graduates'},
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'student_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app01.new_classes': {
            'Meta': {'object_name': 'new_classes'},
            'class_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'course_term': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'limited': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'students': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app01.news': {
            'Meta': {'object_name': 'news'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app01.web_user']"}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'headline': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'news_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'app01.online_course': {
            'Meta': {'object_name': 'online_course'},
            'course_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'course_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'img_link': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'tag_name': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app01.course_tags']", 'symmetrical': 'False'})
        },
        u'app01.questions': {
            'Meta': {'object_name': 'questions'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'display_order': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'})
        },
        u'app01.teachers': {
            'Meta': {'object_name': 'teachers'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introduction': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'social_blog_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'social_blog_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'app01.web_user': {
            'Meta': {'object_name': 'web_user'},
            'class_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app01.class_list']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.CharField', [], {'default': "'user-1.jpg'", 'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app01']