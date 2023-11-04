from django.urls import re_path

from . import views

app_name = 'reports'

urlpatterns = [
    re_path(r'^(?P<year>[0-9]{4})/$', views.AnnualReportView.as_view(), name='annual-report'),
]
