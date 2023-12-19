from django.urls import path
from app1.views import *
app_name='sekhar'
urlpatterns = [
    path('raina/',raina,name='raina'),
]
