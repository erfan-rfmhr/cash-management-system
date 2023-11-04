from django.urls import re_path

from . import views

app_name = 'reports'

urlpatterns = [
    re_path(r'^(?P<year>[0-9]{4})/$', views.AnnualReportView.as_view(), name='annual-report'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.MonthlyReportView.as_view(), name='monthly-report'),
    re_path(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{1,2})/$', views.DailyReportView.as_view(),
            name='daily-report'),
]
