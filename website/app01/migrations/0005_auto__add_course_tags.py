# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'course_tags'
        db.create_table(u'app01_course_tags', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal(u'app01', ['course_tags'])

        # Adding M2M table for field tag_name on 'online_course'
        db.create_table(u'app01_online_course_tag_name', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('online_course', models.ForeignKey(orm[u'app01.online_course'], null=False)),
            ('course_tags', models.ForeignKey(orm[u'app01.course_tags'], null=False))
        ))
        db.create_unique(u'app01_online_course_tag_name', ['online_course_id', 'course_tags_id'])


    def backwards(self, orm):
        # Deleting model 'course_tags'
        db.delete_table(u'app01_course_tags')

        # Removing M2M table for field tag_name on 'online_course'
        db.delete_table('app01_online_course_tag_name')


    models = {
        u'app01.course_tags': {
            'Meta': {'object_name': 'course_tags'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        u'app01.graduates': {
            'Meta': {'object_name': 'graduates'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
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
            'author': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
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