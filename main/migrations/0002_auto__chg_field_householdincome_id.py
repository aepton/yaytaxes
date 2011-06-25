# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'HouseholdIncome.id'
        db.alter_column('main_householdincome', 'id', self.gf('django.db.models.fields.AutoField')(primary_key=True))


    def backwards(self, orm):
        
        # Changing field 'HouseholdIncome.id'
        db.alter_column('main_householdincome', 'id', self.gf('django.db.models.fields.IntegerField')(primary_key=True))


    models = {
        'main.householdincome': {
            'Meta': {'object_name': 'HouseholdIncome'},
            'households': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['main']
