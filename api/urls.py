from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^mb/(?P<mb_id>[0-9]+)/pf/(?P<pf_id>[0-9]+)/msg$', MessageList.as_view()),
    url(r'^mb/(?P<mb_id>[0-9]+)/pf/(?P<pf_id>[0-9]+)/pr$', PrescriptionList.as_view()),
    url(r'^mb/(?P<mb_id>[0-9]+)/pf/(?P<pf_id>[0-9]+)/dur/(?P<bfdate>\w+)$', DurRecordList.as_view()),
    url(r'^mb/(?P<mb_id>[0-9]+)/pf/(?P<pf_id>[0-9]+)/ingredients$', IngreAnalysis.as_view()),

]
