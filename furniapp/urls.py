from django.contrib import admin
from django.urls import path,include,re_path
from furniapp import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    re_path(r'^(?P<id>\d+)/$',views.detail1,name='detail')
]