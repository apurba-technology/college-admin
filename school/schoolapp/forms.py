from django import forms  
from .models import *

class BannerForm(forms.ModelForm): 
  
    class Meta: 
        model = Banner 
        fields = ['name', 'banner_image']



class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = ['title', 'description','attach_file']

class Teacher_dataForm(forms.ModelForm):
    class Meta:
        model = Teacher_data
        fields = ['name', 'deg','img','join_date']

class GalleryForm(forms.ModelForm):
    class Meta:
        model=Gallery
        fields=['title_g', 'images_g']

class TeachernotForm(forms.ModelForm):
    class Meta:
        model=Teachernot
        fields = ['title', 'description','attach_file']

class Events_modForm(forms.ModelForm):
    class Meta:
        model=Events_mod
        fields="__all__"

class Rok_headForm(forms.ModelForm):
    class Meta:
        model=Rok_head
        fields=['title','link']