from django.urls import path
from rest_framework import routers
from hrms import admin
from . import views
from django.conf.urls import url, include
from django.contrib import admin

admin.site.site_header = 'Techlopers Task Management System'
admin.site.index_title = 'Task Management System'
admin.site.site_title = 'Task Management'

"""
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
"""


urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('profile', views.profile),
    path('assign_task', views.task_assign),
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]