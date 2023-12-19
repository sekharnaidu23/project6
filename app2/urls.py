from django.urls import path
from app2.views import *
app_name='naidu'
urlpatterns = [
    path('dhoni/',dhoni,name='dhoni'),
]
