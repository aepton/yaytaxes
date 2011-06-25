# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HouseholdIncome'
        db.create_table('main_householdincome', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('income', self.gf('django.db.models.fields.IntegerField')()),
            ('households', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['HouseholdIncome'])


    def backwards(self, orm):
        
        # Deleting model 'HouseholdIncome'
        db.delete_table('main_householdincome')


    models = {
        'main.householdincome': {
            'Meta': {'object_name': 'HouseholdIncome'},
            'households': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['main']
