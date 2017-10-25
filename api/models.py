# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DatCpTb(models.Model):
    cp_cd = models.CharField(db_column='CP_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    cp_nm = models.CharField(db_column='CP_NM', max_length=255)  # Field name made lowercase.
    cp_kor_nm = models.CharField(db_column='CP_KOR_NM', max_length=255)  # Field name made lowercase.
    cp_desc = models.TextField(db_column='CP_DESC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DAT_CP_TB'


class DatMedTb(models.Model):
    med_cd = models.CharField(db_column='MED_CD', primary_key=True, max_length=10)  # Field name made lowercase.
    cp_cd = models.ForeignKey(DatCpTb, models.DO_NOTHING, db_column='CP_CD')  # Field name made lowercase.
    med_nm = models.CharField(db_column='MED_NM', max_length=255)  # Field name made lowercase.
    med_company_nm = models.CharField(db_column='MED_COMPANY_NM', max_length=255)  # Field name made lowercase.
    med_capa = models.CharField(db_column='MED_CAPA', max_length=255)  # Field name made lowercase.
    med_standard = models.CharField(db_column='MED_STANDARD', max_length=255)  # Field name made lowercase.
    med_unit = models.CharField(db_column='MED_UNIT', max_length=255)  # Field name made lowercase.
    med_pro = models.CharField(db_column='MED_PRO', max_length=255)  # Field name made lowercase.
    med_cate = models.CharField(db_column='MED_CATE', max_length=255)  # Field name made lowercase.
    med_inject = models.CharField(db_column='MED_INJECT', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DAT_MED_TB'


class DurAgeTabooTb(models.Model):
    dat_num = models.AutoField(db_column='DAT_NUM', primary_key=True)  # Field name made lowercase.
    cp_cd = models.CharField(db_column='CP_CD', max_length=255)  # Field name made lowercase.
    dat_age = models.CharField(db_column='DAT_AGE', max_length=255)  # Field name made lowercase.
    dat_age_type = models.CharField(db_column='DAT_AGE_TYPE', max_length=255)  # Field name made lowercase.
    dat_shape = models.CharField(db_column='DAT_SHAPE', max_length=255)  # Field name made lowercase.
    dat_note = models.CharField(db_column='DAT_NOTE', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DUR_AGE_TABOO_TB'


class DurCapaCautTb(models.Model):
    cp_nm = models.CharField(db_column='CP_NM', primary_key=True, max_length=255)  # Field name made lowercase.
    dcc_shape = models.CharField(db_column='DCC_SHAPE', max_length=255)  # Field name made lowercase.
    dcc_max_capa = models.CharField(db_column='DCC_MAX_CAPA', max_length=255)  # Field name made lowercase.
    dcc_note = models.CharField(db_column='DCC_NOTE', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DUR_CAPA_CAUT_TB'
        unique_together = (('cp_nm', 'dcc_shape'),)


class DurCombiTabooTb(models.Model):
    cp_nm_1 = models.CharField(db_column='CP_NM_1', primary_key=True, max_length=255)  # Field name made lowercase.
    cp_nm_2 = models.CharField(db_column='CP_NM_2', max_length=255)  # Field name made lowercase.
    dct_exception = models.CharField(db_column='DCT_EXCEPTION', max_length=255)  # Field name made lowercase.
    dct_note = models.CharField(db_column='DCT_NOTE', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DUR_COMBI_TABOO_TB'
        unique_together = (('cp_nm_1', 'cp_nm_2'),)


class DurEffectCautTb(models.Model):
    cp_nm = models.CharField(db_column='CP_NM', primary_key=True, max_length=255)  # Field name made lowercase.
    dec_effect_group = models.CharField(db_column='DEC_EFFECT_GROUP', max_length=255)  # Field name made lowercase.
    dec_cate_nm = models.CharField(db_column='DEC_CATE_NM', max_length=255)  # Field name made lowercase.
    dec_note = models.CharField(db_column='DEC_NOTE', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DUR_EFFECT_CAUT_TB'


class DurInjectCautTb(models.Model):
    cp_nm = models.CharField(db_column='CP_NM', primary_key=True, max_length=255)  # Field name made lowercase.
    dic_shape = models.CharField(db_column='DIC_SHAPE', max_length=255)  # Field name made lowercase.
    dic_cp_content = models.CharField(db_column='DIC_CP_CONTENT', max_length=255)  # Field name made lowercase.
    dic_max_period = models.CharField(db_column='DIC_MAX_PERIOD', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DUR_INJECT_CAUT_TB'
        unique_together = (('cp_nm', 'dic_shape'),)


class DurOldCautTb(models.Model):
    cp_nm = models.CharField(db_column='CP_NM', primary_key=True, max_length=255)  # Field name made lowercase.
    doc_shape = models.CharField(db_column='DOC_SHAPE', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DUR_OLD_CAUT_TB'
        unique_together = (('cp_nm', 'doc_shape'),)


class MbInfoTb(models.Model):
    mb_id = models.CharField(db_column='MB_ID', primary_key=True, max_length=25)  # Field name made lowercase.
    mb_terms_agr = models.CharField(db_column='MB_TERMS_AGR', max_length=1)  # Field name made lowercase.
    mb_privacy_agr = models.CharField(db_column='MB_PRIVACY_AGR', max_length=1)  # Field name made lowercase.
    mb_reg_dtt = models.DateTimeField(db_column='MB_REG_DTT')  # Field name made lowercase.
    mb_serv_type = models.CharField(db_column='MB_SERV_TYPE', max_length=25)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MB_INFO_TB'


class MbMsgTb(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    pf = models.ForeignKey('MbProfileTb', models.DO_NOTHING, db_column='PF_ID')  # Field name made lowercase.
    msg_num = models.IntegerField(db_column='MSG_NUM')  # Field name made lowercase.
    msg_type = models.CharField(db_column='MSG_TYPE', max_length=255)  # Field name made lowercase.
    msg_val = models.TextField(db_column='MSG_VAL')  # Field name made lowercase.
    msg_dt = models.DateField(db_column='MSG_DT')  # Field name made lowercase.
    msg_time = models.TimeField(db_column='MSG_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MB_MSG_TB'
        unique_together = (('pf', 'msg_num'),)


class MbProfileTb(models.Model):
    pf_id = models.AutoField(db_column='PF_ID', primary_key=True)  # Field name made lowercase.
    mb = models.ForeignKey(MbInfoTb, models.DO_NOTHING, db_column='MB_ID')  # Field name made lowercase.
    pf_rel = models.CharField(db_column='PF_REL', max_length=255)  # Field name made lowercase.
    pf_sex = models.CharField(db_column='PF_SEX', max_length=1)  # Field name made lowercase.
    pf_birth_year = models.CharField(db_column='PF_BIRTH_YEAR', max_length=4)  # Field name made lowercase.
    pf_sido = models.CharField(db_column='PF_SIDO', max_length=255)  # Field name made lowercase.
    pf_sigungu = models.CharField(db_column='PF_SIGUNGU', max_length=255)  # Field name made lowercase.
    pf_create_dtt = models.DateTimeField(db_column='PF_CREATE_DTT')  # Field name made lowercase.
    pf_modify_dtt = models.DateTimeField(db_column='PF_MODIFY_DTT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MB_PROFILE_TB'


class MbPrTb(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    pf = models.ForeignKey(MbProfileTb, models.DO_NOTHING, db_column='PF_ID')  # Field name made lowercase.
    pr_id = models.CharField(db_column='PR_ID', max_length=10)  # Field name made lowercase.
    pr_hosp_nm = models.CharField(db_column='PR_HOSP_NM', max_length=255)  # Field name made lowercase.
    pr_grant_dt = models.DateField(db_column='PR_GRANT_DT')  # Field name made lowercase.
    pr_reg_type = models.CharField(db_column='PR_REG_TYPE', max_length=255)  # Field name made lowercase.
    pr_reg_dtt = models.DateTimeField(db_column='PR_REG_DTT')  # Field name made lowercase.
    pr_img = models.ImageField(null=True, upload_to="prescription_img/")

    class Meta:
        managed = False
        db_table = 'MB_PR_TB'
        unique_together = (('pf', 'pr_id'),)


class MbTmeddTb(models.Model):
    pf = models.ForeignKey('MbTmedTb', models.DO_NOTHING, related_name='profile_id', db_column='PF_ID', primary_key=True)  # Field name made lowercase.
    pr = models.ForeignKey('MbTmedTb', models.DO_NOTHING, related_name='prescription_id', db_column='PR_ID')  # Field name made lowercase.
    tmed_num = models.ForeignKey('MbTmedTb', models.DO_NOTHING, related_name='take_medicine_number', db_column='TMED_NUM')  # Field name made lowercase.
    tmedd_num = models.IntegerField(db_column='TMEDD_NUM')  # Field name made lowercase.
    tmedd_dt = models.DateField(db_column='TMEDD_DT')  # Field name made lowercase.
    tmedd_slot = models.CharField(db_column='TMEDD_SLOT', max_length=255)  # Field name made lowercase.
    tmedd_cfm = models.CharField(db_column='TMEDD_CFM', max_length=1)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MB_TMEDD_TB'
        unique_together = (('pf', 'pr', 'tmed_num', 'tmedd_num'),)


# class MbTmedTb(models.Model):
#     pf = models.ForeignKey('MbPrTb', models.DO_NOTHING, related_name='profile_id', db_column='PF_ID', primary_key=True)  # Field name made lowercase.
#     pr = models.ForeignKey('MbPrTb', models.DO_NOTHING, related_name='prescription_id', db_column='PR_ID')  # Field name made lowercase.
#     tmed_num = models.IntegerField(db_column='TMED_NUM')  # Field name made lowercase.
#     med_cd = models.ForeignKey('DatMedTb', models.DO_NOTHING, db_column='MED_CD')  # Field name made lowercase.
#     tmed_qty = models.IntegerField(db_column='TMED_QTY')  # Field name made lowercase.
#     tmed_times = models.IntegerField(db_column='TMED_TIMES')  # Field name made lowercase.
#     tmed_day_cnt = models.IntegerField(db_column='TMED_DAY_CNT')  # Field name made lowercase.
#     tmed_start_dt = models.DateField(db_column='TMED_START_DT')  # Field name made lowercase.
#     tmed_end_dt = models.DateField(db_column='TMED_END_DT')  # Field name made lowercase.
#     tmed_modify_dtt = models.DateTimeField(db_column='TMED_MODIFY_DTT')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'MB_TMED_TB'
#         unique_together = (('pf', 'pr', 'tmed_num'),)


class MbTmedTb(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    pf_id = models.IntegerField(db_column='PF_ID')  # Field name made lowercase.
    pr_id = models.CharField(db_column='PR_ID', max_length=10)  # Field name made lowercase.
    tmed_num = models.IntegerField(db_column='TMED_NUM')  # Field name made lowercase.
    med_cd = models.CharField(db_column='MED_CD', max_length=10)  # Field name made lowercase.
    tmed_qty = models.IntegerField(db_column='TMED_QTY')  # Field name made lowercase.
    tmed_times = models.IntegerField(db_column='TMED_TIMES')  # Field name made lowercase.
    tmed_day_cnt = models.IntegerField(db_column='TMED_DAY_CNT')  # Field name made lowercase.
    tmed_start_dt = models.DateField(db_column='TMED_START_DT')  # Field name made lowercase.
    tmed_end_dt = models.DateField(db_column='TMED_END_DT')  # Field name made lowercase.
    tmed_modify_dtt = models.DateTimeField(db_column='TMED_MODIFY_DTT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MB_TMED_TB'
        unique_together = (('pf_id', 'pr_id', 'tmed_num'),)


class SysCddTb(models.Model):
    cdg = models.ForeignKey('SysCdgTb', models.DO_NOTHING, db_column='CDG_ID', primary_key=True)  # Field name made lowercase.
    cdd_id = models.CharField(db_column='CDD_ID', max_length=255)  # Field name made lowercase.
    cdd_val = models.CharField(db_column='CDD_VAL', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SYS_CDD_TB'
        unique_together = (('cdg', 'cdd_id'),)


class SysCdgTb(models.Model):
    cdg_id = models.CharField(db_column='CDG_ID', primary_key=True, max_length=25)  # Field name made lowercase.
    cdg_nm = models.CharField(db_column='CDG_NM', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SYS_CDG_TB'


class SysCntTb(models.Model):
    cnt_id = models.CharField(db_column='CNT_ID', primary_key=True, max_length=25)  # Field name made lowercase.
    cnt_val = models.IntegerField(db_column='CNT_VAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SYS_CNT_TB'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
