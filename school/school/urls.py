"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from schoolapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    #path('admin', views.admin),
    path('banner_upload', views.banner_upload, name='banner_upload'), 
    path('notice_up', views.notice_upload),
    path('ev',views.events),
    
    path('gallery_up',views.gallery_up),
    path('display_gallery',views.disg),
    path('display_banner',views.disb),
    path('display_notice',views.disn, name='display_notice'),
    path('delete_notice/<int:id>', views.delete_notice),
    path('delete_banner/<int:id>', views.delete_banner),
    path('delete_gallery/<int:id>', views.dele_gallery, name='delete_gallery'),
    path('delete_events/<int:id>',views.delete_events),
    path('delete_head/<int:id>',views.delete_head),
    path('delete_teacher_not/<int:id>',views.delete_teach_not),
    path('delete_teacher_data/<int:id>',views.delete_teach_data),
    path('teacher_not_up', views.teacher_notice_up),
    path('mission',views.mission),
    path('fee',views.fee),
    path('press_note',views.press_note),
    path('history',views.history),
    path('excutive_teacher',views.excutive_teacher),
    path('administor-off',views.administor_off),
    path('adminstration',views.adminstration),
    path('contact',views.contact),
    path('te',views.teachers),
    path('ro',views.rok),
    path('display_head',views.headline),
    path('display_t_not',views.Teacher_notice_d),
    path('display_teach_data',views.teacher_data_display, name='display_teach_data'),
    path('disply_event',views.events_d),
    ######################
    path('admin', views.ind),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('reset', views.reset),
    path('wall', views.wall),
  
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)