from django.contrib import admin
from .models import *

class DatCpTbAdmin(admin.ModelAdmin):
    list_display = ('cp_cd', 'cp_nm', 'cp_kor_nm', 'cp_desc')


class DatMedTbAdmin(admin.ModelAdmin):
    list_display = ('med_cd', 'cp_cd', 'med_nm', 'med_company_nm', 'med_capa', 'med_standard', 'med_unit', 'med_pro', 'med_cate', 'med_inject')


class DurAgeTabooTbAdmin(admin.ModelAdmin):
    list_display = ('dat_num', 'cp_cd', 'dat_age', 'dat_age_type', 'dat_shape', 'dat_note')


class DurCapaCautTbAdmin(admin.ModelAdmin):
    list_display = ('cp_nm', 'dcc_shape', 'dcc_max_capa', 'dcc_note')


class DurCombiTabooTbAdmin(admin.ModelAdmin):
    list_display = ('cp_nm_1', 'cp_nm_2', 'dct_exception', 'dct_note')


class DurEffectCautTbAdmin(admin.ModelAdmin):
    list_display = ('cp_nm', 'dec_effect_group', 'dec_cate_nm', 'dec_note')


class DurInjectCautTbAdmin(admin.ModelAdmin):
    list_display = ('cp_nm', 'dic_shape', 'dic_cp_content', 'dic_max_period')


class DurOldCautTbAdmin(admin.ModelAdmin):
    list_display = ('cp_nm', 'doc_shape')


class MbInfoTbAdmin(admin.ModelAdmin):
    list_display = ('mb_id', 'mb_terms_agr', 'mb_privacy_agr', 'mb_reg_dtt', 'mb_serv_type')


class MbMsgTbAdmin(admin.ModelAdmin):
    list_display = ('pf', 'msg_num', 'msg_type', 'msg_val', 'msg_dt', 'msg_time')


class MbProfileTbAdmin(admin.ModelAdmin):
    list_display = ('pf_id', 'mb', 'pf_rel', 'pf_sex', 'pf_birth_year', 'pf_sido', 'pf_sigungu', 'pf_create_dtt', 'pf_modify_dtt')


class MbPrTbAdmin(admin.ModelAdmin):
    list_display = ('pf', 'pr_id', 'pr_hosp_nm', 'pr_grant_dt', 'pr_reg_type', 'pr_reg_dtt')


class MbTmeddTbAdmin(admin.ModelAdmin):
    list_display = ('pf', 'pr', 'tmed_num', 'tmedd_num', 'tmedd_dt', 'tmedd_slot', 'tmedd_cfm')


# class MbTmedTbAdmin(admin.ModelAdmin):
#     list_display = ('pf', 'pr', 'tmed_num', 'med_cd', 'tmed_qty', 'tmed_times', 'tmed_day_cnt', 'tmed_start_dt', 'tmed_end_dt', 'tmed_modify_dtt')

class MbTmedTbAdmin(admin.ModelAdmin):
    list_display = ('id', 'pf_id', 'pr_id', 'tmed_num', 'med_cd', 'tmed_qty', 'tmed_times', 'tmed_day_cnt', 'tmed_start_dt', 'tmed_end_dt', 'tmed_modify_dtt')


class SysCddTbAdmin(admin.ModelAdmin):
    list_display = ('cdg', 'cdd_id', 'cdd_val')


class SysCdgTbAdmin(admin.ModelAdmin):
    list_display = ('cdg_id', 'cdg_nm')


class SysCntTbAdmin(admin.ModelAdmin):
    list_display = ('cnt_id', 'cnt_val')


class DjangoSessionAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'session_data', 'expire_date')


admin.site.register(DatCpTb, DatCpTbAdmin)
admin.site.register(DatMedTb, DatMedTbAdmin)
admin.site.register(DurAgeTabooTb, DurAgeTabooTbAdmin)
admin.site.register(DurCapaCautTb, DurCapaCautTbAdmin)
admin.site.register(DurCombiTabooTb, DurCombiTabooTbAdmin)
admin.site.register(DurEffectCautTb, DurEffectCautTbAdmin)
admin.site.register(DurInjectCautTb, DurInjectCautTbAdmin)
admin.site.register(DurOldCautTb, DurOldCautTbAdmin)
admin.site.register(MbInfoTb, MbInfoTbAdmin)
admin.site.register(MbMsgTb, MbMsgTbAdmin)
admin.site.register(MbProfileTb, MbProfileTbAdmin)
admin.site.register(MbPrTb, MbPrTbAdmin)
admin.site.register(MbTmeddTb, MbTmeddTbAdmin)
admin.site.register(MbTmedTb, MbTmedTbAdmin)
admin.site.register(SysCddTb, SysCddTbAdmin)
admin.site.register(SysCdgTb, SysCdgTbAdmin)
admin.site.register(SysCntTb, SysCntTbAdmin)
admin.site.register(DjangoSession, DjangoSessionAdmin)
