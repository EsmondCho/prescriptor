from .models import *
from .disableCSRF import CsrfExemptSessionAuthentication

from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

# from django.db.models import Q

from django.core.files.base import ContentFile
import base64

from PIL import Image
import pytesseract

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication

from .disableCSRF import CsrfExemptSessionAuthentication
from .models import *

from django.http import HttpResponse
import json

from datetime import datetime


# dur 안걸리면 0, 걸리면 걸린 dur 수
def check_age_dur(med_code_list):

    ingre_code_list = []

    for code in med_code_list:
        med = DatMedTb.objects.filter(med_cd=code)
        if med:
            ingre_code_list.append(med[0].cp_cd.cp_cd)
            print(med[0].cp_cd.cp_cd)

    num = 0

    for code in ingre_code_list:
        if DurAgeTabooTb.objects.filter(cp_cd=code):
            num += 1

    return num


class MessageList(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, mb_id, pf_id):

        pf = MbProfileTb.objects.get(pf_id=pf_id)
        msgs = MbMsgTb.objects.filter(pf=pf)

        msg_list = []

        for msg in msgs:
            dic = {}
            dic['msg_type'] = msg.msg_type
            dic['msg_val'] = msg.msg_val
            dic['msg_dt'] = str(msg.msg_dt)
            dic['msg_time'] = str(msg.msg_time)
            msg_list.append(dic)
            print(msg.msg_val)

        return HttpResponse(json.dumps(msg_list), content_type='application/json', status=status.HTTP_200_OK)



class PrescriptionList(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request, mb_id, pf_id):

        form = request.FILES

        # print("______________")
        # print(form)
        # print("______________")

        print(request.FILES)

        img_file = form['image']

        pf = MbProfileTb.objects.get(pf_id=pf_id)

        pr_cnt = SysCntTb.objects.get(cnt_id="PRESCRIPTION_ID")
        pr_cnt.cnt_val += 1
        pr_cnt.save()

        pr = MbPrTb.objects.create(
            id = MbPrTb.objects.count() + 1,
            pf = pf,
            pr_id = "P"+str(pr_cnt.cnt_val),
            pr_hosp_nm = "test",
            pr_grant_dt = "2017-10-22",
            pr_reg_type = "123",
            pr_reg_dtt = "2017-10-22 00:21:52",
            pr_img=img_file
        )
        pr.save()

        # 처방 의약품 코드 리스트
        detected_list = pytesseract.image_to_string(Image.open(pr.pr_img.path)).split("\n")

        detected_med_code_list = []

        for med_code in detected_list:
            print(med_code.replace(" ", ""))
            detected_med_code_list.append(med_code.replace(" ", ""))

        # detected_med_code_list = ['644100410', '654004860']

        # 복약기록정보 생성
        for code in detected_med_code_list:
            mb_tmed = MbTmedTb.objects.create(
                id = MbTmedTb.objects.count() + 1,
                pf_id = pf.pf_id,
                pr_id = pr.pr_id,
                tmed_num = MbTmedTb.objects.count() + 1,
                med_cd = code,
                tmed_qty = 0,
                tmed_times = 0,
                tmed_day_cnt = 0,
                tmed_start_dt = '2017-01-01',
                tmed_end_dt = '2019-01-01',
                tmed_modify_dtt = '2017-10-22 00:21:52'
            )
            mb_tmed.save()

        # 메인화면 메시지 생성
        print(detected_med_code_list)
        checked_num = check_age_dur(detected_med_code_list)
        print("checked_num : " + str(checked_num))

        if checked_num == 0:
            msg = MbMsgTb.objects.create(
                id = MbMsgTb.objects.count() + 1,
                pf = pf,
                msg_num = MbMsgTb.objects.count() + 1,
                msg_type = "registered",
                msg_val = "새로운 처방전을 등록하셨군요! 등록된 복약 정보를 확인하세요!", # 내용 고민중
                msg_dt = datetime.today().strftime('%Y-%m-%d'),
                msg_time = datetime.now().strftime('%H:%M:%S')
            )
            msg.save()

        else:
            msg = MbMsgTb.objects.create(
                id=MbMsgTb.objects.count() + 1,
                pf = pf,
                msg_num = MbMsgTb.objects.count() + 1,
                msg_type = "registered_dur",
                msg_val="새로운 처방전을 등록하셨군요! 등록된 복용 기간동안\n\n연령금기(" + str(checked_num) + ")\n\n" + "가 발견되었습니다.",
                msg_dt=datetime.today().strftime('%Y-%m-%d'),
                msg_time=datetime.now().strftime('%H:%M:%S')
            )
            msg.save()

        # 처방 의약품 이름 리스트
        med_name_list = []
        for code in detected_med_code_list:
            meds = DatMedTb.objects.filter(med_cd=code)
            if meds:
                med_name_list.append(meds[0].med_nm)
                print(meds[0].med_nm)

        return HttpResponse(json.dumps(med_name_list), content_type='application/json', status=status.HTTP_201_CREATED)


class DurRecordList(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, mb_id, pf_id, bfdate):

        year = bfdate[:4]
        month = bfdate[5:7]
        day = bfdate[-2:]

        bfdate = year + "-" + month + "-" + day
        end_date = datetime.strptime(bfdate, '%Y-%m-%d').date()

        # msg_list = MbMsgTb.objects.filter(msg_dt__range=["2000-01-01", end_date])
        #
        # for msg in msg_list:
        #     print(msg.msg_val)

        tmeds = MbTmedTb.objects.filter(pf_id=pf_id)

        ingre_code_list = []

        for tmed in tmeds:
            med = DatMedTb.objects.filter(med_cd=tmed.med_cd)
            dic = {}

            if med:
                dic['tmed_start_dt'] = str(tmed.tmed_start_dt)
                dic['tmed_end_dt'] = str(tmed.tmed_end_dt)
                dic['ingre_code'] = med[0].cp_cd.cp_cd
                dic['med_name'] = med[0].med_nm
                ingre_code_list.append(dic)

        date_taboo_list = []

        for code in ingre_code_list:
            print(code['ingre_code'])
            taboo_list = DurAgeTabooTb.objects.filter(cp_cd=code['ingre_code'])
            if taboo_list:
                for taboo in taboo_list:
                    dic = {}
                    dic['tmed_start_dt'] = code['tmed_start_dt']
                    dic['tmed_end_dt'] = code['tmed_end_dt']
                    dic['agetaboo'] = str(taboo.dat_age) + str(taboo.dat_age_type) + " / " + str(code['med_name'])
                    date_taboo_list.append(dic)

        return HttpResponse(json.dumps(date_taboo_list), content_type='application/json', status=status.HTTP_200_OK)


class IngreAnalysis(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)

    def get(self, request, mb_id, pf_id):

        tmeds = MbTmedTb.objects.filter(pf_id=pf_id)

        ingre_name_list = []

        for tmed in tmeds:
            med = DatMedTb.objects.get(med_cd=tmed.med_cd)
            ingre_name_list.append(med.cp_cd.cp_nm)

        # 중복 제거
        ingre_name_list = list(set(ingre_name_list))

        return HttpResponse(json.dumps(ingre_name_list), content_type='application/json', status=status.HTTP_200_OK)
