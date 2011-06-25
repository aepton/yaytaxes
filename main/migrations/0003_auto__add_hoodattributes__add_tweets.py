# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'HoodAttributes'
        db.create_table('main_hoodattributes', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('attributes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('main', ['HoodAttributes'])

        # Adding model 'Tweets'
        db.create_table('main_tweets', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('tweet_text', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('service', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('budget_amount', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['Tweets'])


    def backwards(self, orm):
        
        # Deleting model 'HoodAttributes'
        db.delete_table('main_hoodattributes')

        # Deleting model 'Tweets'
        db.delete_table('main_tweets')


    models = {
        'main.hoodattributes': {
            'Meta': {'object_name': 'HoodAttributes'},
            'attributes': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'main.householdincome': {
            'Meta': {'object_name': 'HouseholdIncome'},
            'households': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'income': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.tweets': {
            'Meta': {'object_name': 'Tweets'},
            'budget_amount': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'tweet_text': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'user': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']
