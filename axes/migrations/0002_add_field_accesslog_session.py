# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from ..utils import get_session_model

Session = get_session_model()


session_orm_label = '%s.%s' % (Session._meta.app_label, Session._meta.object_name)
session_model_label = '%s.%s' % (Session._meta.app_label, Session._meta.module_name)


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AccessLog.session'
        db.add_column(u'axes_accesslog', 'session',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm[session_orm_label], null=True, on_delete=models.SET_NULL),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AccessLog.session'
        db.delete_column(u'axes_accesslog', 'session_id')


    models = {
        u'axes.accessattempt': {
            'Meta': {'ordering': "['-attempt_time']", 'object_name': 'AccessAttempt'},
            'attempt_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'failures_since_start': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'get_data': ('django.db.models.fields.TextField', [], {}),
            'http_accept': ('django.db.models.fields.CharField', [], {'max_length': '1025'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'post_data': ('django.db.models.fields.TextField', [], {}),
            'trusted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        u'axes.accesslog': {
            'Meta': {'ordering': "['-attempt_time']", 'object_name': 'AccessLog'},
            'attempt_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'http_accept': ('django.db.models.fields.CharField', [], {'max_length': '1025'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'logout_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['%s']" % session_orm_label, 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'trusted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user_agent': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        session_model_label: {
            'Meta': {'object_name': 'Session'},
            Session._meta.pk.attname: ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
        }
    }

    complete_apps = ['axes']