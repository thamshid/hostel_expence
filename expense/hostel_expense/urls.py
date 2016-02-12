from django.conf.urls import patterns, url
from hostel_expense import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name="Index"),
    url(r'^chart/$', views.chart, name="chart"),
    url(r'^month_chart$', views.month_chart, name="month_chart"),
    url(r'^login$', views.login, name="login"),
    url(r'^authenticate$', views.authenticate, name="authenticate"),
    url(r'^add_expense$', views.add_expense, name="add_expense"),
    url(r'^individual_expense$', views.individual_expense, name="individual_expense"),
   



)
