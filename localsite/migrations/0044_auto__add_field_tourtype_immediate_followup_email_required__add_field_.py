# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'TourType.immediate_followup_email_required'
        db.add_column('localsite_tourtype', 'immediate_followup_email_required', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'TourType.immediate_followup_email_subject'
        db.add_column('localsite_tourtype', 'immediate_followup_email_subject', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'TourType.immediate_followup_email_body'
        db.add_column('localsite_tourtype', 'immediate_followup_email_body', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'TourType.prior_to_tour_email_required'
        db.add_column('localsite_tourtype', 'prior_to_tour_email_required', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'TourType.prior_to_tour_email_hours'
        db.add_column('localsite_tourtype', 'prior_to_tour_email_hours', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True), keep_default=False)

        # Adding field 'TourType.prior_to_tour_email_subject'
        db.add_column('localsite_tourtype', 'prior_to_tour_email_subject', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Adding field 'TourType.prior_to_tour_email_body'
        db.add_column('localsite_tourtype', 'prior_to_tour_email_body', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'TourType.immediate_followup_email_required'
        db.delete_column('localsite_tourtype', 'immediate_followup_email_required')

        # Deleting field 'TourType.immediate_followup_email_subject'
        db.delete_column('localsite_tourtype', 'immediate_followup_email_subject')

        # Deleting field 'TourType.immediate_followup_email_body'
        db.delete_column('localsite_tourtype', 'immediate_followup_email_body')

        # Deleting field 'TourType.prior_to_tour_email_required'
        db.delete_column('localsite_tourtype', 'prior_to_tour_email_required')

        # Deleting field 'TourType.prior_to_tour_email_hours'
        db.delete_column('localsite_tourtype', 'prior_to_tour_email_hours')

        # Deleting field 'TourType.prior_to_tour_email_subject'
        db.delete_column('localsite_tourtype', 'prior_to_tour_email_subject')

        # Deleting field 'TourType.prior_to_tour_email_body'
        db.delete_column('localsite_tourtype', 'prior_to_tour_email_body')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'localsite.cartguest': {
            'Meta': {'object_name': 'CartGuest'},
            'cart_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guests'", 'to': "orm['shop.CartItem']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        'localsite.comboschedule': {
            'Meta': {'unique_together': "(('tourschedule', 'tourtype', 'days_after'),)", 'object_name': 'ComboSchedule'},
            'days_after': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tourschedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localsite.TourSchedule']"}),
            'tourtype': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localsite.TourType']"})
        },
        'localsite.dayofweek': {
            'Meta': {'object_name': 'DayOfWeek'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isoweekday': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16'})
        },
        'localsite.ordercompletedsiteskin': {
            'Meta': {'object_name': 'OrderCompletedSiteSkin'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Order']", 'unique': 'True'}),
            'site_skin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localsite.SiteSkin']"})
        },
        'localsite.orderconfirmationbannertext': {
            'Meta': {'object_name': 'OrderConfirmationBannerText'},
            'banner_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'header_top_text': ('django.db.models.fields.TextField', [], {'default': "'25% REFUND FOR ALL MISSED TOURS'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site_skin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localsite.SiteSkin']", 'unique': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'localsite.orderconfirmationcoupon': {
            'Meta': {'ordering': "('order',)", 'object_name': 'OrderConfirmationCoupon'},
            'coupon_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'site_skin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localsite.SiteSkin']"})
        },
        'localsite.orderconfirmationsection': {
            'Meta': {'ordering': "('order',)", 'object_name': 'OrderConfirmationSection'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'site_skin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localsite.SiteSkin']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'localsite.orderconfirmationsubsection': {
            'Meta': {'ordering': "('order',)", 'object_name': 'OrderConfirmationSubSection'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sub_sections'", 'to': "orm['localsite.OrderConfirmationSection']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'localsite.orderhash': {
            'Meta': {'object_name': 'OrderHash'},
            'hash': ('common.db_fields.RandomHashField', [], {'default': "'c69a88dccae6114567169ed7c0d8221e'", 'unique': 'True', 'max_length': '128', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Order']", 'unique': 'True'}),
            'void_failed': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'localsite.overbookingattempt': {
            'Meta': {'object_name': 'OverbookingAttempt'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_overbooked': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'occurred_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'tour': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'overbookings'", 'to': "orm['localsite.TourProduct']"})
        },
        'localsite.siteskin': {
            'Meta': {'object_name': 'SiteSkin'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '16', 'db_index': 'True'}),
            'concierge_lp_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'concierge_reg_ui_banner': ('django.db.models.fields.files.ImageField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'conversion_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'custom_css': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'favicon': ('django.db.models.fields.files.FileField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'hash': ('common.db_fields.RandomHashField', [], {'default': "'81b089ba2be64483c804b4c0828ad066'", 'unique': 'True', 'max_length': '128', 'update_on_save': 'True', 'db_index': 'True'}),
            'header_banner_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '128'}),
            'header_banner_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_concierge_cta': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_default': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'order_confirmation_contact_info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'order_confirmation_logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '128'}),
            'reseller_lp_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'toc_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'toc_text': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'tour_page_step1_text': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'})
        },
        'localsite.surveyemailsent': {
            'Meta': {'object_name': 'SurveyEmailSent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['shop.Order']", 'unique': 'True'})
        },
        'localsite.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('satchmo_utils.thumbnail.field.ImageWithThumbnailField', [], {'max_length': '128', 'auto_rename': 'True'}),
            'job_title': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'localsite.tourcapacity': {
            'Meta': {'object_name': 'TourCapacity'},
            'day_of_week': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localsite.DayOfWeek']", 'symmetrical': 'False'}),
            'from_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seats_available': ('django.db.models.fields.IntegerField', [], {}),
            'to_date': ('django.db.models.fields.DateField', [], {}),
            'tour_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'capacities'", 'to': "orm['localsite.TourType']"}),
            'updated_on': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'localsite.tourcategory': {
            'Meta': {'ordering': "('order',)", 'object_name': 'TourCategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'site_skins': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['localsite.SiteSkin']", 'null': 'True', 'blank': 'True'})
        },
        'localsite.tourguest': {
            'Meta': {'object_name': 'TourGuest'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'order_item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'guests'", 'to': "orm['shop.OrderItem']"})
        },
        'localsite.tourproduct': {
            'Meta': {'unique_together': "(('tour_type', 'day', 'tour_time'),)", 'object_name': 'TourProduct'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'day': ('django.db.models.fields.DateField', [], {'db_index': 'True'}),
            'overbooking_attempts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'product': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['product.Product']", 'unique': 'True', 'primary_key': 'True'}),
            'schedule': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localsite.TourSchedule']", 'null': 'True', 'blank': 'True'}),
            'tour_time': ('django.db.models.fields.TimeField', [], {}),
            'tour_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localsite.TourType']"})
        },
        'localsite.tourschedule': {
            'Meta': {'object_name': 'TourSchedule'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'day_of_week': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['localsite.DayOfWeek']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tour_time': ('django.db.models.fields.TimeField', [], {}),
            'tour_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'schedules'", 'to': "orm['localsite.TourType']"})
        },
        'localsite.tourtype': {
            'Meta': {'ordering': "('-active', 'order', 'name')", 'object_name': 'TourType'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'allow_refunds': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'base_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tours'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['localsite.TourCategory']"}),
            'combo_schedules': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['localsite.TourSchedule']", 'null': 'True', 'through': "orm['localsite.ComboSchedule']", 'blank': 'True'}),
            'customer_names_page_explanation': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'customer_names_page_headline': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'default_commission': ('django.db.models.fields.DecimalField', [], {'default': "'0.00'", 'max_digits': '5', 'decimal_places': '2'}),
            'default_site_skin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['localsite.SiteSkin']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'has_brochures': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '128', 'blank': 'True'}),
            'immediate_followup_email_body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'immediate_followup_email_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'immediate_followup_email_subject': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'in_perfect_inventory': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_combo': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_inventory_public': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'is_tour_available_to_concierges': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_tour_available_to_resellers': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'max_calendar_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'min_calendar_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'option_group': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'tour_types'", 'null': 'True', 'to': "orm['product.OptionGroup']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'prior_to_tour_email_body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'prior_to_tour_email_hours': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prior_to_tour_email_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prior_to_tour_email_subject': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'requires_names': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rollover_off': ('django.db.models.fields.files.ImageField', [], {'max_length': '128', 'blank': 'True'}),
            'rollover_on': ('django.db.models.fields.files.ImageField', [], {'max_length': '128', 'blank': 'True'}),
            'seats_available': ('django.db.models.fields.IntegerField', [], {}),
            'sell_in_even_quantities_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '128', 'blank': 'True'})
        },
        'product.category': {
            'Meta': {'ordering': "['site', 'parent__id', 'ordering', 'name']", 'unique_together': "(('site', 'slug'),)", 'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'child'", 'null': 'True', 'to': "orm['product.Category']"}),
            'related_categories': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_categories_rel_+'", 'null': 'True', 'to': "orm['product.Category']"}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'})
        },
        'product.optiongroup': {
            'Meta': {'ordering': "['sort_order', 'name']", 'object_name': 'OptionGroup'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'sort_order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'product.product': {
            'Meta': {'ordering': "('site', 'ordering', 'name')", 'unique_together': "(('site', 'sku'), ('site', 'slug'))", 'object_name': 'Product'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'also_purchased': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'also_purchased_rel_+'", 'null': 'True', 'to': "orm['product.Product']"}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['product.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'height_units': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_in_stock': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '18', 'decimal_places': '6'}),
            'length': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'length_units': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'ordering': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'related_items': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'related_items_rel_+'", 'null': 'True', 'to': "orm['product.Product']"}),
            'shipclass': ('django.db.models.fields.CharField', [], {'default': "'DEFAULT'", 'max_length': '10'}),
            'short_description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'sku': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'db_index': 'True', 'max_length': '255', 'blank': 'True'}),
            'taxClass': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.TaxClass']", 'null': 'True', 'blank': 'True'}),
            'taxable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_sold': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '18', 'decimal_places': '6'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'weight_units': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '6', 'decimal_places': '2', 'blank': 'True'}),
            'width_units': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        'product.taxclass': {
            'Meta': {'object_name': 'TaxClass'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'shop.cart': {
            'Meta': {'object_name': 'Cart'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contact.Contact']", 'null': 'True', 'blank': 'True'}),
            'date_time_created': ('django.db.models.fields.DateTimeField', [], {}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"})
        },
        'shop.cartitem': {
            'Meta': {'ordering': "('id',)", 'object_name': 'CartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Cart']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.Product']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '6'})
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
        'shop.orderitem': {
            'Meta': {'ordering': "('id',)", 'object_name': 'OrderItem'},
            'completed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'discount': ('satchmo_utils.fields.CurrencyField', [], {'null': 'True', 'max_digits': '18', 'decimal_places': '10', 'blank': 'True'}),
            'expire_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'line_item_price': ('satchmo_utils.fields.CurrencyField', [], {'max_digits': '18', 'decimal_places': '10'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shop.Order']"}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['product.Product']"}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '18', 'decimal_places': '6'}),
            'tax': ('satchmo_utils.fields.CurrencyField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'}),
            'unit_price': ('satchmo_utils.fields.CurrencyField', [], {'max_digits': '18', 'decimal_places': '10'}),
            'unit_tax': ('satchmo_utils.fields.CurrencyField', [], {'default': "'0.00'", 'max_digits': '18', 'decimal_places': '10'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['localsite']
