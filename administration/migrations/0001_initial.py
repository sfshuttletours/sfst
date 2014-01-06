# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'ConciergeMessage'
        db.create_table('administration_conciergemessage', (
            ('concierge', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['concierges.Concierge'], null=True)),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('is_global', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True, blank=True)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('administration', ['ConciergeMessage'])

        # Adding model 'InventoryDayNote'
        db.create_table('administration_inventorydaynote', (
            ('note', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('for_date', self.gf('django.db.models.fields.DateField')()),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('administration', ['InventoryDayNote'])
    
    
    def backwards(self, orm):
        
        # Deleting model 'ConciergeMessage'
        db.delete_table('administration_conciergemessage')

        # Deleting model 'InventoryDayNote'
        db.delete_table('administration_inventorydaynote')
    
    
    models = {
        'administration.conciergemessage': {
            'Meta': {'object_name': 'ConciergeMessage'},
            'concierge': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['concierges.Concierge']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_global': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True', 'blank': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        },
        'administration.inventorydaynote': {
            'Meta': {'object_name': 'InventoryDayNote'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'for_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'concierges.concierge': {
            'Meta': {'object_name': 'Concierge'},
            'booking_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'concierges'", 'to': "orm['contact.Contact']"}),
            'email_notifications': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'hotel_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('satchmo_utils.thumbnail.field.ImageWithThumbnailField', [], {'max_length': '128', 'auto_rename': 'True', 'blank': 'True'}),
            'orders': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['shop.Order']", 'null': 'True', 'blank': 'True'}),
            'per_week': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'send_checks_to': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'create_date': ('django.db.models.fields.DateField', [], {}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contact.Organization']", 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contact.ContactRole']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        'contact.contactorganization': {
            'Meta': {'object_name': 'ContactOrganization'},
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'contact.contactorganizationrole': {
            'Meta': {'object_name': 'ContactOrganizationRole'},
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'contact.contactrole': {
            'Meta': {'object_name': 'ContactRole'},
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'contact.organization': {
            'Meta': {'object_name': 'Organization'},
            'create_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'notes': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contact.ContactOrganizationRole']", 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contact.ContactOrganization']", 'null': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'shop.order': {
            'Meta': {'object_name': 'Order'},
            'bill_addressee': ('django.db.models.fields.CharField', [], {'max_length': '61', 'blank': 'True'}),
            'bill_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'bill_country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'bill_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'bill_state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'bill_street1': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'bill_street2': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'contact': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contact.Contact']"}),
            'discount': ('satchmo_utils.fields.CurrencyField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'}),
            'discount_code': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ship_addressee': ('django.db.models.fields.CharField', [], {'max_length': '61', 'blank': 'True'}),
            'ship_city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ship_country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'ship_postal_code': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'ship_state': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ship_street1': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'ship_street2': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'shipping_cost': ('satchmo_utils.fields.CurrencyField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'}),
            'shipping_description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shipping_discount': ('satchmo_utils.fields.CurrencyField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'}),
            'shipping_method': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shipping_model': ('shipping.fields.ShippingChoiceCharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'sub_total': ('satchmo_utils.fields.CurrencyField', [], {'display_decimal': '4', 'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'}),
            'tax': ('satchmo_utils.fields.CurrencyField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'}),
            'time_stamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'total': ('satchmo_utils.fields.CurrencyField', [], {'display_decimal': '4', 'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }
    
    complete_apps = ['administration']
