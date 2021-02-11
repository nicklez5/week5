# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from product import views
app_name = 'random_app'
urlpatterns = [
        path('',views.random_app_list,name='random_app_list'),
        path('<int:random_app_id>/',views.random_app_detail,name='random_app_detail'),
        path('new/',views.random_app_new,name='random_app_new'),
        path('<int:random_app_id>/update',views.random_app_update,name='random_app_update'),
]
# Create your views here.
