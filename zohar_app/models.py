# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Items(models.Model):
    items = models.IntegerField(db_column='Items', primary_key=True)  # Field name made lowercase.
    item_name = models.CharField(db_column='Item-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_class = models.CharField(db_column='Item-Class', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'items'


class MModels(models.Model):
    m_model_code = models.IntegerField(db_column='M-model-code', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m_model_name = models.CharField(db_column='M-model-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'm-models'


class MainItems(models.Model):
    main_items_code = models.IntegerField(db_column='Main-items-code', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    main_item_name = models.CharField(db_column='Main-item-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'main-items'


class MainSites(models.Model):
    site_code = models.CharField(db_column='Site-code', primary_key=True, max_length=6)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    site_name = models.CharField(db_column='Site-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_site_name = models.CharField(db_column='Sub-Site-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'main-sites'


class Manufacturer(models.Model):
    manufacturer_code = models.IntegerField(db_column='manufacturerCode', primary_key=True)  # Field renamed to remove unsuitable characters.
    manufacturer_name = models.CharField(db_column='manufacturerName', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m_model_code = models.IntegerField(db_column='MModelCode')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'manufacturer'


class Statuses(models.Model):
    itemstatuscode = models.IntegerField(db_column='ItemStatusCode', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    itemstatus = models.CharField(db_column='ItemStatus', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'statuses'


class Survey(models.Model):
    barcode = models.CharField(db_column='BarCode',  max_length=12)  # Field name made lowercase.
    id = models.IntegerField(db_column='id',primary_key=True)# Field name made lowercase.
    item = models.IntegerField(db_column='Item')  # Field name made lowercase.
    item_name = models.CharField(db_column='Item-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_class = models.CharField(db_column='Item-Class', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_status = models.IntegerField(db_column='Item-Status')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manufacturer_code = models.IntegerField(db_column='Manufacturer-code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m_model_code = models.IntegerField(db_column='M-model-code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m_serial = models.IntegerField(db_column='M-serial')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    piba_name = models.CharField(db_column='PIBA-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    main_item_name = models.CharField(db_column='Main-item-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    main_item_code = models.IntegerField(db_column='Main-Item-code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    site_code = models.IntegerField(db_column='Site-code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_site_name = models.CharField(db_column='Sub-Site-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.CharField(db_column='Location', max_length=20)  # Field name made lowercase.
    checked_by = models.CharField(db_column='Checked-by', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    checked_date = models.DateField(db_column='Checked-date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    remarks = models.CharField(db_column='Remarks', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey'


class Survey1(models.Model):
    barcode = models.CharField(db_column='BarCode', primary_key=True, max_length=12)  # Field name made lowercase.
    item = models.IntegerField(db_column='Item')  # Field name made lowercase.
    item_name = models.CharField(db_column='Item-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_class = models.CharField(db_column='Item-Class', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    item_status = models.IntegerField(db_column='Item-Status')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    manufacturer_code = models.IntegerField(db_column='Manufacturer-code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m_model_code = models.IntegerField(db_column='M-model-code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    m_serial = models.IntegerField(db_column='M-serial')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    piba_name = models.CharField(db_column='PIBA-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    main_item_name = models.CharField(db_column='Main-item-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    main_item_code = models.IntegerField(db_column='Main-Item-code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    site_code = models.IntegerField(db_column='Site-code')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sub_site_name = models.CharField(db_column='Sub-Site-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location = models.CharField(db_column='Location', max_length=20)  # Field name made lowercase.
    checked_by = models.CharField(db_column='Checked-by', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    checked_date = models.DateField(db_column='Checked-date')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    remarks = models.CharField(db_column='Remarks', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'survey1'
