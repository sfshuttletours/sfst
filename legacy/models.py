# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=80)
    class Meta:
        db_table = u'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    group = models.ForeignKey("AuthGroup")
    permission = models.ForeignKey("AuthPermission")
    class Meta:
        db_table = u'auth_group_permissions'

class AuthMessage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey("AuthUser")
    message = models.TextField()
    class Meta:
        db_table = u'auth_message'

class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    class Meta:
        db_table = u'auth_permission'

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    is_superuser = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        db_table = u'auth_user'

class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey("AuthUser")
    group = models.ForeignKey("AuthGroup")
    class Meta:
        db_table = u'auth_user_groups'

class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey("AuthUser")
    permission = models.ForeignKey("AuthPermission")
    class Meta:
        db_table = u'auth_user_user_permissions'

class CommentsComment(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey("AuthUser")
    content_type = models.ForeignKey("DjangoContentType")
    object_id = models.IntegerField()
    headline = models.CharField(max_length=255)
    comment = models.TextField()
    rating1 = models.PositiveSmallIntegerField(null=True, blank=True)
    rating2 = models.PositiveSmallIntegerField(null=True, blank=True)
    rating3 = models.PositiveSmallIntegerField(null=True, blank=True)
    rating4 = models.PositiveSmallIntegerField(null=True, blank=True)
    rating5 = models.PositiveSmallIntegerField(null=True, blank=True)
    rating6 = models.PositiveSmallIntegerField(null=True, blank=True)
    rating7 = models.PositiveSmallIntegerField(null=True, blank=True)
    rating8 = models.PositiveSmallIntegerField(null=True, blank=True)
    valid_rating = models.BooleanField()
    submit_date = models.DateTimeField()
    is_public = models.BooleanField()
    ip_address = models.CharField(max_length=15, blank=True)
    is_removed = models.BooleanField()
    site_id = models.IntegerField()
    class Meta:
        db_table = u'comments_comment'

class CommentsFreecomment(models.Model):
    id = models.IntegerField(primary_key=True)
    content_type = models.ForeignKey("DjangoContentType")
    object_id = models.IntegerField()
    comment = models.TextField()
    person_name = models.CharField(max_length=50)
    submit_date = models.DateTimeField()
    is_public = models.BooleanField()
    ip_address = models.CharField(max_length=15)
    approved = models.BooleanField()
    site_id = models.IntegerField()
    class Meta:
        db_table = u'comments_freecomment'

class CommentsKarmascore(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey("AuthUser")
    comment = models.ForeignKey("CommentsComment")
    score = models.SmallIntegerField()
    scored_date = models.DateTimeField()
    class Meta:
        db_table = u'comments_karmascore'

class CommentsModeratordeletion(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey("AuthUser")
    comment = models.ForeignKey("CommentsComment")
    deletion_date = models.DateTimeField()
    class Meta:
        db_table = u'comments_moderatordeletion'

class CommentsUserflag(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey("AuthUser")
    comment = models.ForeignKey("CommentsComment")
    flag_date = models.DateTimeField()
    class Meta:
        db_table = u'comments_userflag'

class ConfigurationLongsetting(models.Model):
    id = models.IntegerField(primary_key=True)
    site = models.ForeignKey("DjangoSite")
    group = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    value = models.TextField()
    class Meta:
        db_table = u'configuration_longsetting'

class ConfigurationSetting(models.Model):
    id = models.IntegerField(primary_key=True)
    site = models.ForeignKey("DjangoSite")
    group = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    class Meta:
        db_table = u'configuration_setting'

class ContactAddressbook(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey("ContactContact")
    description = models.CharField(max_length=20)
    street1 = models.CharField(max_length=50)
    street2 = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    is_default_shipping = models.BooleanField()
    is_default_billing = models.BooleanField()
    class Meta:
        db_table = u'contact_addressbook'

class ContactContact(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey("AuthUser", null=True, blank=True)
    role = models.CharField(max_length=20, blank=True)
    organization = models.ForeignKey("ContactOrganization", null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=75)
    notes = models.TextField()
    create_date = models.DateField()
    class Meta:
        db_table = u'contact_contact'

class ContactDownloadlink(models.Model):
    id = models.IntegerField(primary_key=True)
    downloadable_product_id = models.IntegerField()
    order = models.ForeignKey("ContactOrder")
    key = models.CharField(max_length=40)
    num_attempts = models.IntegerField()
    time_stamp = models.DateTimeField()
    active = models.BooleanField()
    class Meta:
        db_table = u'contact_downloadlink'

class ContactInteraction(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey("ContactContact")
    type = models.CharField(max_length=30)
    date_time = models.DateTimeField()
    description = models.TextField()
    class Meta:
        db_table = u'contact_interaction'

class ContactOrder(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey("ContactContact")
    ship_street1 = models.CharField(max_length=50)
    ship_street2 = models.CharField(max_length=50)
    ship_city = models.CharField(max_length=50)
    ship_state = models.CharField(max_length=50)
    ship_postal_code = models.CharField(max_length=10)
    ship_country = models.CharField(max_length=50)
    bill_street1 = models.CharField(max_length=50)
    bill_street2 = models.CharField(max_length=50)
    bill_city = models.CharField(max_length=50)
    bill_state = models.CharField(max_length=50)
    bill_postal_code = models.CharField(max_length=10)
    bill_country = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    sub_total = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    total = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    discount_code = models.CharField(max_length=20, blank=True)
    discount = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    method = models.CharField(max_length=50)
    shipping_description = models.CharField(max_length=50, blank=True)
    shipping_method = models.CharField(max_length=50, blank=True)
    shipping_model = models.CharField(max_length=30, blank=True)
    shipping_cost = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    shipping_discount = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    tax = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20)
    class Meta:
        db_table = u'contact_order'



class ContactOrderitem(models.Model):
    id = models.IntegerField(primary_key=True)
    insurance = models.BooleanField()
    order = models.ForeignKey("ContactOrder")
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=None, decimal_places=None)
    unit_tax = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    line_item_price = models.DecimalField(max_digits=None, decimal_places=None)
    tax = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    expire_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField()
    discount = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    class Meta:
        db_table = u'contact_orderitem'

    def __unicode__(self):
        s = 'Quantity: %s' % self.quantity
        for d in self.contactorderitemdetail_set.all():
            s += d.name + ': ' + d.value + ', '
        return s

class ContactOrderitemdetail(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.ForeignKey("ContactOrderitem")
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    price_change = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    sort_order = models.IntegerField()
    class Meta:
        db_table = u'contact_orderitemdetail'

class ContactOrderpayment(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey("ContactOrder")
    payment = models.CharField(max_length=25)
    amount = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    transaction_id = models.CharField(max_length=25, blank=True)
    class Meta:
        db_table = u'contact_orderpayment'

class ContactOrderstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey("ContactOrder")
    status = models.CharField(max_length=20)
    notes = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    class Meta:
        db_table = u'contact_orderstatus'

class ContactOrdertaxdetail(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey("ContactOrder")
    method = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    tax = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    class Meta:
        db_table = u'contact_ordertaxdetail'

class ContactOrdervariable(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey("ContactOrder")
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)
    class Meta:
        db_table = u'contact_ordervariable'

class ContactOrganization(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    role = models.CharField(max_length=30)
    create_date = models.DateField()
    notes = models.TextField(blank=True)
    class Meta:
        db_table = u'contact_organization'

class ContactPhonenumber(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey("ContactContact")
    type = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)
    primary = models.BooleanField()
    class Meta:
        db_table = u'contact_phonenumber'

class ContactReseller(models.Model):
    id = models.IntegerField(primary_key=True)
    cid = models.IntegerField()
    commission = models.CharField(max_length=9)
    discount = models.CharField(max_length=9)
    discount2 = models.CharField(max_length=9)
    special = models.BooleanField()
    coname = models.CharField(max_length=30)
    class Meta:
        db_table = u'contact_reseller'

class ContactResellerrequest(models.Model):
    id = models.IntegerField(primary_key=True)
    web = models.CharField(max_length=9999)
    rtype = models.CharField(max_length=9999)
    email = models.CharField(max_length=9999)
    lname = models.CharField(max_length=9999)
    phone = models.CharField(max_length=9999)
    cname = models.CharField(max_length=9999)
    fname = models.CharField(max_length=9999)
    tourmonths = models.CharField(max_length=9999)
    desc = models.CharField(max_length=9999)
    class Meta:
        db_table = u'contact_resellerrequest'

    def __unicode__(self):
        s = """
web: %s
rtype: %s
email: %s
lname: %s
phone: %s
cname: %s
fname: %s
tourmonths: %s
desc: %s
        """ % (self.web, self.rtype, self.email, self.lname, self.phone, self.cname, self.fname, self.tourmonths, self.desc)
        return s

class DiscountDiscount(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=100)
    code = models.CharField(unique=True, max_length=20)
    amount = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    percentage = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    automatic = models.BooleanField(null=True, blank=True)
    alloweduses = models.IntegerField(null=True, db_column=u'allowedUses', blank=True) # Field name made lowercase.
    numuses = models.IntegerField(null=True, db_column=u'numUses', blank=True) # Field name made lowercase.
    minorder = models.DecimalField(decimal_places=None, null=True, max_digits=None, db_column=u'minOrder', blank=True) # Field name made lowercase.
    startdate = models.DateField(db_column=u'startDate') # Field name made lowercase.
    enddate = models.DateField(db_column=u'endDate') # Field name made lowercase.
    active = models.BooleanField()
    freeshipping = models.BooleanField(null=True, db_column=u'freeShipping', blank=True) # Field name made lowercase.
    includeshipping = models.BooleanField(null=True, db_column=u'includeShipping', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'discount_discount'

class DiscountDiscountValidproducts(models.Model):
    id = models.IntegerField(primary_key=True)
    discount = models.ForeignKey("DiscountDiscount")
    product = models.ForeignKey("ProductProduct")
    class Meta:
        db_table = u'discount_discount_validProducts'

class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)
    action_time = models.DateTimeField()
    user_id = models.IntegerField()
    content_type_id = models.IntegerField(null=True, blank=True)
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    class Meta:
        db_table = u'django_admin_log'

class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    class Meta:
        db_table = u'django_content_type'

class DjangoFlatpage(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    content = models.TextField()
    enable_comments = models.BooleanField()
    template_name = models.CharField(max_length=70)
    registration_required = models.BooleanField()
    class Meta:
        db_table = u'django_flatpage'

class DjangoFlatpageSites(models.Model):
    id = models.IntegerField(primary_key=True)
    flatpage = models.ForeignKey("DjangoFlatpage")
    site = models.ForeignKey("DjangoSite")
    class Meta:
        db_table = u'django_flatpage_sites'

class DjangoSession(models.Model):
    session_key = models.CharField(max_length=40, primary_key=True)
    session_data = models.TextField()
    expire_date = models.DateTimeField()
    class Meta:
        db_table = u'django_session'

class DjangoSite(models.Model):
    id = models.IntegerField(primary_key=True)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    class Meta:
        db_table = u'django_site'

class L10NAdminarea(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey("L10NCountry")
    name = models.CharField(max_length=60)
    abbrev = models.CharField(max_length=3, blank=True)
    active = models.BooleanField()
    class Meta:
        db_table = u'l10n_adminarea'

class L10NCountry(models.Model):
    id = models.IntegerField(primary_key=True)
    iso2_code = models.CharField(unique=True, max_length=2)
    name = models.CharField(max_length=128)
    printable_name = models.CharField(max_length=128)
    iso3_code = models.CharField(unique=True, max_length=3)
    numcode = models.PositiveSmallIntegerField(null=True, blank=True)
    active = models.BooleanField()
    continent = models.CharField(max_length=2)
    admin_area = models.CharField(max_length=2, blank=True)
    class Meta:
        db_table = u'l10n_country'

class PaymentCreditcarddetail(models.Model):
    id = models.IntegerField(primary_key=True)
    orderpayment = models.ForeignKey("ContactOrderpayment")
    credittype = models.CharField(max_length=16, db_column=u'creditType') # Field name made lowercase.
    displaycc = models.CharField(max_length=4, db_column=u'displayCC') # Field name made lowercase.
    encryptedcc = models.CharField(max_length=40, db_column=u'encryptedCC', blank=True) # Field name made lowercase.
    expiremonth = models.IntegerField(db_column=u'expireMonth') # Field name made lowercase.
    expireyear = models.IntegerField(db_column=u'expireYear') # Field name made lowercase.
    class Meta:
        db_table = u'payment_creditcarddetail'

class PaymentPaymentoption(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=20)
    active = models.BooleanField()
    optionname = models.CharField(unique=True, max_length=20, db_column=u'optionName') # Field name made lowercase.
    sortorder = models.IntegerField(db_column=u'sortOrder') # Field name made lowercase.
    class Meta:
        db_table = u'payment_paymentoption'

class ProductCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=50)
    parent_id = models.IntegerField(null=True, blank=True)
    meta = models.TextField(blank=True)
    description = models.TextField()
    ordering = models.IntegerField()
    class Meta:
        db_table = u'product_category'

class ProductCategoryimage(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey("ProductCategory", null=True, blank=True)
    picture = models.CharField(max_length=100)
    caption = models.CharField(max_length=100, blank=True)
    sort = models.IntegerField()
    class Meta:
        db_table = u'product_categoryimage'

class ProductCategoryimagetranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    categoryimage = models.ForeignKey("ProductCategoryimage")
    languagecode = models.CharField(max_length=10)
    caption = models.CharField(max_length=255)
    version = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'product_categoryimagetranslation'

class ProductCategorytranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.ForeignKey("ProductCategory")
    languagecode = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    version = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'product_categorytranslation'

class ProductConfigurableproduct(models.Model):
    product = models.ForeignKey("ProductProduct")
    create_subs = models.BooleanField()
    class Meta:
        db_table = u'product_configurableproduct'

class ProductConfigurableproductOptionGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    configurableproduct = models.ForeignKey("ProductConfigurableproduct")
    optiongroup = models.ForeignKey("ProductOptiongroup")
    class Meta:
        db_table = u'product_configurableproduct_option_group'

class ProductCustomproduct(models.Model):
    product = models.ForeignKey("ProductProduct")
    downpayment = models.IntegerField()
    deferred_shipping = models.BooleanField()
    class Meta:
        db_table = u'product_customproduct'

class ProductCustomproductOptionGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    customproduct = models.ForeignKey("ProductCustomproduct")
    optiongroup = models.ForeignKey("ProductOptiongroup")
    class Meta:
        db_table = u'product_customproduct_option_group'

class ProductCustomtextfield(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=50)
    products = models.ForeignKey("ProductCustomproduct")
    sort_order = models.IntegerField()
    price_change = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    class Meta:
        db_table = u'product_customtextfield'

class ProductCustomtextfieldtranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    customtextfield = models.ForeignKey("ProductCustomtextfield")
    languagecode = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    version = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'product_customtextfieldtranslation'

class ProductDatetimeschema(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey("ProductProduct")
    hour = models.CharField(max_length=2)
    minute = models.CharField(max_length=2)
    ampm = models.CharField(max_length=2)
    weekdays = models.BooleanField()
    weekends = models.BooleanField()
    notes = models.CharField(max_length=9999)
    class Meta:
        db_table = u'product_datetimeschema'

    def __unicode__(self):
        return '%s %s:%s %sampm %s' % (self.product.name, self.hour, self.minute, self.ampm, ('weekdays' if self.weekdays else 'weekends'))

    def get_nice_data(self):
        from datetime import time
        hour = int(self.hour) + 12 if self.ampm != '0' else int(self.hour)
        t = time(hour, int(self.minute))
        weekdays = []
        if self.weekdays:
            weekdays = [1, 2, 3, 4, 5]
        if self.weekends:
            weekdays += [6, 7]
        return (t, weekdays)


class ProductDatetimeschema2(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey("ProductMultiproduct")
    dts = models.ForeignKey("ProductDatetimeschema")
    class Meta:
        db_table = u'product_datetimeschema2'

class ProductDownloadableproduct(models.Model):
    product = models.ForeignKey("ProductProduct")
    file = models.CharField(max_length=100)
    num_allowed_downloads = models.IntegerField()
    expire_minutes = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'product_downloadableproduct'

class ProductKind(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    class Meta:
        db_table = u'product_kind'

class ProductMultiproduct(models.Model):
    product_ptr = models.ForeignKey("ProductProduct")
    discount = models.IntegerField()
    class Meta:
        db_table = u'product_multiproduct'

class ProductMultiproductProducts(models.Model):
    id = models.IntegerField(primary_key=True)
    multiproduct = models.ForeignKey("ProductMultiproduct")
    product = models.ForeignKey("ProductProduct")
    class Meta:
        db_table = u'product_multiproduct_products'

class ProductOption(models.Model):
    id = models.IntegerField(primary_key=True)
    optiongroup = models.ForeignKey("ProductOptiongroup", db_column=u'optionGroup_id') # Field name made lowercase.
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    price_change = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    displayorder = models.IntegerField(db_column=u'displayOrder') # Field name made lowercase.
    class Meta:
        db_table = u'product_option'

class ProductOptiongroup(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    sort_order = models.IntegerField()
    class Meta:
        db_table = u'product_optiongroup'

class ProductOptiongrouptranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    optiongroup = models.ForeignKey("ProductOptiongroup")
    languagecode = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    version = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'product_optiongrouptranslation'

class ProductOptiontranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    option = models.ForeignKey("ProductOption")
    languagecode = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    version = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'product_optiontranslation'

class ProductPrice(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey("ProductProduct")
    price = models.DecimalField(max_digits=None, decimal_places=None)
    quantity = models.IntegerField()
    expires = models.DateField(null=True, blank=True)
    kind = models.ForeignKey("ProductKind", null=True, blank=True)
    class Meta:
        db_table = u'product_price'

class ProductProduct(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=50)
    sku = models.CharField(unique=True, max_length=255, blank=True)
    short_description = models.TextField()
    description = models.TextField()
    items_in_stock = models.IntegerField()
    meta = models.TextField(blank=True)
    date_added = models.DateField(null=True, blank=True)
    active = models.BooleanField()
    featured = models.BooleanField()
    ordering = models.IntegerField()
    insurancefee = models.IntegerField(db_column=u'insuranceFee') # Field name made lowercase.
    numseats = models.IntegerField(db_column=u'numSeats') # Field name made lowercase.
    weight = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    weight_units = models.CharField(max_length=3, blank=True)
    length = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    length_units = models.CharField(max_length=3, blank=True)
    width = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    width_units = models.CharField(max_length=3, blank=True)
    height = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    height_units = models.CharField(max_length=3, blank=True)
    total_sold = models.IntegerField()
    taxable = models.BooleanField()
    taxclass_id = models.IntegerField(null=True, db_column=u'taxClass_id', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'product_product'

class ProductProductAlsoPurchased(models.Model):
    id = models.IntegerField(primary_key=True)
    from_product = models.ForeignKey("ProductProduct")
    to_product = models.ForeignKey("ProductProduct")
    class Meta:
        db_table = u'product_product_also_purchased'

class ProductProductCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey("ProductProduct")
    category = models.ForeignKey("ProductCategory")
    class Meta:
        db_table = u'product_product_category'

class ProductProductRelatedItems(models.Model):
    id = models.IntegerField(primary_key=True)
    from_product = models.ForeignKey("ProductProduct")
    to_product = models.ForeignKey("ProductProduct")
    class Meta:
        db_table = u'product_product_related_items'

class ProductProductattribute(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey("ProductProduct")
    languagecode = models.CharField(max_length=10, blank=True)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    class Meta:
        db_table = u'product_productattribute'

class ProductProductimage(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey("ProductProduct", null=True, blank=True)
    picture = models.CharField(max_length=100)
    caption = models.CharField(max_length=100, blank=True)
    sort = models.IntegerField()
    class Meta:
        db_table = u'product_productimage'

class ProductProductimagetranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    productimage = models.ForeignKey("ProductProductimage")
    languagecode = models.CharField(max_length=10)
    caption = models.CharField(max_length=255)
    version = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'product_productimagetranslation'

class ProductProducttranslation(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey("ProductProduct")
    languagecode = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    description = models.TextField()
    version = models.IntegerField()
    active = models.BooleanField()
    class Meta:
        db_table = u'product_producttranslation'

class ProductProductvariation(models.Model):
    product = models.ForeignKey("ProductProduct")
    parent = models.ForeignKey("ProductConfigurableproduct")
    class Meta:
        db_table = u'product_productvariation'

class ProductProductvariationOptions(models.Model):
    id = models.IntegerField(primary_key=True)
    productvariation = models.ForeignKey("ProductProductvariation")
    option = models.ForeignKey("ProductOption")
    class Meta:
        db_table = u'product_productvariation_options'

class ProductSubscriptionproduct(models.Model):
    product = models.ForeignKey("ProductProduct")
    recurring = models.BooleanField()
    recurring_times = models.IntegerField(null=True, blank=True)
    expire_days = models.IntegerField(null=True, blank=True)
    is_shippable = models.IntegerField()
    class Meta:
        db_table = u'product_subscriptionproduct'

class ProductTourday(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    product = models.ForeignKey("ProductProduct")
    seatsfilled = models.IntegerField(db_column=u'seatsFilled') # Field name made lowercase.
    notes = models.CharField(max_length=9999)
    numberofseats = models.IntegerField(db_column=u'numberOfSeats') # Field name made lowercase.
    class Meta:
        db_table = u'product_tourday'
    def __unicode__(self):
        return '%s:%s- %s' % (self.date, self.time, self.product.name)

class ProductTrial(models.Model):
    id = models.IntegerField(primary_key=True)
    subscription = models.ForeignKey("ProductSubscriptionproduct")
    price = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    expire_days = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'product_trial'

class ShopCart(models.Model):
    id = models.IntegerField(primary_key=True)
    desc = models.CharField(max_length=10, blank=True)
    date_time_created = models.DateTimeField()
    customer_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'shop_cart'

class ShopCartitem(models.Model):
    id = models.IntegerField(primary_key=True)
    cart = models.ForeignKey("ShopCart")
    product_id = models.IntegerField()
    quantity = models.CharField(max_length=99999)
    chosen_date = models.CharField(max_length=99999)
    insurance = models.IntegerField()
    class Meta:
        db_table = u'shop_cartitem'

class ShopCartitemdetails(models.Model):
    id = models.IntegerField(primary_key=True)
    cartitem = models.ForeignKey("ShopCartitem")
    value = models.TextField()
    name = models.CharField(max_length=100)
    price_change = models.DecimalField(null=True, max_digits=None, decimal_places=None, blank=True)
    sort_order = models.IntegerField()
    class Meta:
        db_table = u'shop_cartitemdetails'

class ShopConfig(models.Model):
    site = models.ForeignKey("DjangoSite")
    store_name = models.CharField(unique=True, max_length=100)
    store_description = models.TextField(blank=True)
    store_email = models.CharField(max_length=75, blank=True)
    street1 = models.CharField(max_length=50, blank=True)
    street2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=30, blank=True)
    postal_code = models.CharField(max_length=9, blank=True)
    country_id = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    no_stock_checkout = models.BooleanField()
    in_country_only = models.BooleanField()
    sales_country_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'shop_config'

class ShopConfigShippingCountries(models.Model):
    id = models.IntegerField(primary_key=True)
    config = models.ForeignKey("ShopConfig")
    country = models.ForeignKey("L10NCountry")
    class Meta:
        db_table = u'shop_config_shipping_countries'

class SupplierRawitem(models.Model):
    id = models.IntegerField(primary_key=True)
    supplier = models.ForeignKey("ContactOrganization")
    supplier_num = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    unit_cost = models.DecimalField(max_digits=None, decimal_places=None)
    inventory = models.IntegerField()
    class Meta:
        db_table = u'supplier_rawitem'

class SupplierSupplierorder(models.Model):
    id = models.IntegerField(primary_key=True)
    supplier = models.ForeignKey("ContactOrganization")
    date_created = models.DateField()
    order_sub_total = models.DecimalField(max_digits=None, decimal_places=None)
    order_shipping = models.DecimalField(max_digits=None, decimal_places=None)
    order_tax = models.DecimalField(max_digits=None, decimal_places=None)
    order_notes = models.CharField(max_length=200)
    order_total = models.DecimalField(max_digits=None, decimal_places=None)
    class Meta:
        db_table = u'supplier_supplierorder'

class SupplierSupplierorderitem(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey("SupplierSupplierorder")
    line_item = models.ForeignKey("SupplierRawitem")
    line_item_quantity = models.IntegerField()
    line_item_total = models.DecimalField(max_digits=None, decimal_places=None)
    class Meta:
        db_table = u'supplier_supplierorderitem'

class SupplierSupplierorderstatus(models.Model):
    id = models.IntegerField(primary_key=True)
    order = models.ForeignKey("SupplierSupplierorder")
    status = models.CharField(max_length=20)
    notes = models.CharField(max_length=100)
    date = models.DateTimeField()
    class Meta:
        db_table = u'supplier_supplierorderstatus'

class TaxTaxclass(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    class Meta:
        db_table = u'tax_taxclass'

class TaxTaxrate(models.Model):
    id = models.IntegerField(primary_key=True)
    taxclass = models.ForeignKey("TaxTaxclass", db_column=u'taxClass_id') # Field name made lowercase.
    taxzone = models.ForeignKey("L10NAdminarea", null=True, db_column=u'taxZone_id', blank=True) # Field name made lowercase.
    taxcountry = models.ForeignKey("L10NCountry", null=True, db_column=u'taxCountry_id', blank=True) # Field name made lowercase.
    percentage = models.DecimalField(max_digits=None, decimal_places=None)
    class Meta:
        db_table = u'tax_taxrate'

class WishlistProductwish(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.ForeignKey("ContactContact")
    product = models.ForeignKey("ProductProduct")
    _details = models.TextField(blank=True)
    create_date = models.DateTimeField()
    class Meta:
        db_table = u'wishlist_productwish'

