from django.shortcuts import render, redirect
from django.http import HttpResponse
from schoolapp.functions.functions import handle_uploaded_file
from schoolapp.forms import *
from django.contrib import messages
 
# Create your views here.
def index(request):
    if request.method == 'GET':
        Banners = Banner.objects.all() 
        Notices = Notice.objects.order_by('-id')
        Gallerys = Gallery.objects.order_by('-id') 
        Event = Events_mod.objects.order_by('-id')
        Teachernots = Teachernot.objects.order_by('-id')
        rok1 = Rok_head.objects.order_by('-id')
        return render(request, 'index.html', {'Note' : Notices, 'banner_images' : Banners, 'gal' : Gallerys,'Even':Event, 'teach':Teachernots, 'rok':rok1 })



def admin(request):
    return render(request, "admin.html")

def banner_upload(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        return redirect('/display_banner')
    else:
        form = BannerForm()
    return render(request,'banner_up.html',{'form': form})



def events(request):
    if request.method == 'POST':
        b=Events_modForm(request.POST)
        bb=Events_mod()
        bb.events_name=request.POST['events_name']
        bb.events_link=request.POST['events_link']
        bb.save()
        return redirect('/disply_event')
    else:
        b=Events_modForm()
        return render(request,'events_up.html',{'form':b})




def notice_upload(request):
    if request.method == 'POST':
        fo = NoticeForm(request.POST, request.FILES)
        
        if fo.is_valid():
            fo.save()
        return redirect('/display_notice')
    else:
        fo= NoticeForm()
    return render(request,'notice_u.html',{'form': fo})
    #return render(request,'notice_u.html',{'form': fo})
def teacher_notice_up(request):
    if request.method == 'POST':
        foot = TeachernotForm(request.POST, request.FILES)
        
        if foot.is_valid():
            foot.save()
        return redirect('/display_t_not')
    else:
        foot= TeachernotForm()
    return render(request,'teacher_not_up.html',{'form': foot})

def disg(request): 
  
    if request.method == 'GET':
        Gallerys = Gallery.objects.all() 
        
        return render(request, 'gallery.html',{'gal' : Gallerys})

def disb(request): 
  
    if request.method == 'GET':
        Banners = Banner.objects.all()  
        return render(request, 'banner_d.html',{'banner_images' : Banners})

def headline(request): 
  
    if request.method == 'GET':
        Rok2 = Rok_head.objects.all()  
        return render(request, 'head_d.html',{'rok' : Rok2})

def teacher_data_display(request): 
  
    if request.method == 'GET':
        Rok5 = Teacher_data.objects.all()  
        return render(request, 'teacher_d_display.html',{'rok4' : Rok5})

def events_d(request): 
  
    if request.method == 'GET':
        Rok55 = Events_mod.objects.all()  
        return render(request, 'event_display.html',{'rok44' : Rok55})

def disn(request): 
  
    if request.method == 'GET':
        Notices = Notice.objects.order_by('-id')  
        return render(request, 'notice_d.html',{'Note' : Notices})
def Teacher_notice_d(request): 
  
    if request.method == 'GET':
        Noti = Teachernot.objects.order_by('-id')  
        return render(request, 't_notice_d.html',{'Note' : Noti})




def gallery_up(request):
    if request.method == 'POST':
        fo1 = GalleryForm(request.POST, request.FILES)
        
        if fo1.is_valid():
            fo1.save()
            return redirect('/display_gallery')
            
    else:
        fo1 = GalleryForm()
    return render(request,'gallery_up.html',{'form': fo1})


def delete_notice(request, id):
    Notices = Notice.objects.get(id=id)
    Notices.delete()
    return redirect("display_notice")
def delete_banner(request, id):
    Banners = Banner.objects.get(id=id)
    Banners.delete()
    return redirect("/display_banner")
def dele_gallery(request, id):
    Gallerys = Gallery.objects.get(id=id)
    Gallerys.delete()
    return redirect('/display_gallery')
def delete_events(request, id):
    ev = Events_mod.objects.get(id=id)
    ev.delete()
    return redirect('/disply_event')

def delete_head(request, id):
    head1 = Rok_head.objects.get(id=id)
    head1.delete()
    return redirect('/display_head')
def delete_teach_data(request, id):
    tea = Teacher_data.objects.get(id=id)
    tea.delete()
    return redirect('/display_teach_data')

def delete_teach_not(request, id):
    teach = Teachernot.objects.get(id=id)
    teach.delete()
    return redirect('/display_t_not')

def mission(request):
    return render(request, "mission.html")


def fee(request):
    return render(request,"fee.html")

def press_note(request):
    return render(request,"press_n.html")


def history(request):
    return render(request,"orgi.html")

def excutive_teacher(request):
    return render(request,"excutive_t.html")

def administor_off(request):
    return render(request,"administor-off.html")

def adminstration(request):
    return render(request,"adminstration.html")

def contact(request):
    return render(request,"contact.html")

def teachers(request):
    if request.method == 'POST':
        fo2 = Teacher_dataForm(request.POST, request.FILES)
        
        if fo2.is_valid():
            fo2.save()
            return redirect('display_teach_data')
            
    else:
        fo2 = Teacher_dataForm()
    return render(request,'teacher_data.html',{'form': fo2})

def rok(request):
    
    if request.method == 'POST':
        fo3 = Rok_headForm(request.POST)
        if fo3.is_valid():
            fo3.save()
            return redirect('/display_head')
    else:
        fo3 = Rok_headForm()
    return render(request,'he.html',{'form':fo3})


###############################################################
##########################################################################
# Create your views here.
def ind(request):
    if 'user_id' in request.session:
        return redirect('/success')
    else:
        return render(request, 'ind.html')


def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.add_message(request, messages.ERROR, value, extra_tags='register')
            return redirect('/admin')
        else:
            pw_hash = (request.POST['password'].encode())
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
            request.session['user_id'] = user.id
            return redirect("/success")
    else:
        return redirect("/admin")


def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.add_message(request, messages.ERROR, value, extra_tags='login')
            return redirect('/admin')
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['user_id'] = user.id
            return redirect("/wall")


def wall(request):
    if 'user_id' not in request.session:
        return redirect('/admin')
    else:
        context = {
            "user": User.objects.get(id=request.session['user_id'])
        }
        return render(request,'Admin.html', context)


def success(request):
    if 'user_id' not in request.session:
        return redirect('/admin')
    else:
        context = {
            "user": User.objects.get(id=request.session['user_id'])
        }
        return redirect('/wall', context)


def reset(request):
    if 'user_id' not in request.session:
        return redirect('/admin')
    else:
        request.session.clear()
        print("session has been cleared")
        return redirect("/admin")