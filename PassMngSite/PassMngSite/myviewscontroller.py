from bootstrap_modal_forms.generic import  BSModalFormView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.password_validation import password_changed
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.hashers import *
from cryptography.fernet import Fernet
from django.urls import reverse_lazy
from PassMngSite import *
from argon2 import PasswordHasher
from django.core.mail import send_mail
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.template.loader import get_template
import datetime
from jinja2 import Template
from PassMngSite.myapp.models import PassEntry
from PassMngSite.myapp.forms import ChangePassword
###############################################################################################################
###############################################################################################################
from PassMngSite.myapp import forms


def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")

def singleblog(request):
    return render(request, "single-blog.html")

def registerlogin(request):  # makhsoose namayesh page register
    return render(request, "registerlogin.html")

def register(request):
    if request.method == 'POST':  # daryafte valu ha az karbar va sabt dar db.
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password1 = request.POST["password1"]
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'username taken before', fail_silently=True)
                return redirect("registerlogin")
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'email taken before')
                return redirect("registerlogin")
            else:
                user = User.objects.create_user(username=username, email=email, password=password,
                                                first_name=first_name, last_name=last_name)
                user.save();
                messages.error(request, 'Successful Registration ...')
                return redirect("/")
        else:
            messages.error(request, 'Passwords does not match...')
            return redirect("registerlogin")
    else:
        return render(request, "registerlogin.html")

def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        global uid
        uid = User.objects.filter(username=username).values("id")#select id from user
        uid = uid[0]#print first index of dict <QuerySet [{'id': 11}]>
        uid = uid['id']#print dict {'id': 11}
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid Credential')
            return redirect('registerlogin')
    else:
        return render(request, "registerlogin.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def passentry(request):
    return render(request, "passentry.html")

def passentrysubmit(request):  # main form//user pass to func
    if request.method == 'POST':
        username = request.POST["user_name"]
        servicename = request.POST["service_name"]
        desc = request.POST["desc_comm"]
        pas = request.POST["pass_word"]
        hashpas = make_password(pas, hasher='argon2') #hash password
        passent = PassEntry.objects.create(user_name=username, pass_word=hashpas, service_name=servicename,
                                           desc_comm=desc, user_id_id=uid)
        seki = Fernet.generate_key()
        pas = str.encode(pas)#convert to byte
        f = Fernet(seki)#yek instance
        tok = f.encrypt(pas)
        with open('PassMngSite/binsp.bin', 'ab') as mybin:#save to file
            mybin.write(b'\n')#line 1 khali.
            mybin.write(str(passent.user_id_id).encode())
            mybin.write(b'\n')
            mybin.write(str(passent.id).encode())#int to byte--row of insert
            mybin.write(b'\n')
            mybin.write(seki)
            mybin.write(b'\n')
            mybin.write(tok)
            mybin.write(b'\n')
        passent.save();
    return redirect("/")

#@permission_required("myapp.view_passentry")
def elements(request):
    passentry = PassEntry.objects.filter(user_id_id=11).all()#all row which id=13// a Dict // get return only one//
    passentrycount = PassEntry.objects.filter(user_id_id=11).count()
    passentrycount = range(1,passentrycount+1) #convert to range of 1 to 9
    with open('PassMngSite/binsp.bin', 'rb') as mybinall:
              _all = mybinall.readlines() #read all file in array
    with open('PassMngSite/binsp.bin', 'rb') as mybin:
             lineid=1
             _sekitok = []
             kitok = mybin.readline()
             for line in mybin:
                 lineid+=1
                 kitok = line.strip()#all line in mybin--remove space
                 if kitok == b'11':#str(11).encode():#uid=11
                    _seki = _all[lineid+1]
                    _tok = _all[lineid+2]
                    _sekitok1 = _sekitok.append(_seki) #all key & token marboot b id=11
                    _sekitok2 = _sekitok.append(_tok)
    all_pass=[]
    for id in range(0,len(_sekitok),2):
        _seki = Fernet(_sekitok[id])
        _pas = _seki.decrypt(_sekitok[id+1])
        _pas = _pas.decode("utf-8")  # convert byte to text
        _allpas = all_pass.append(_pas) #make list of all pass
    return render(request, "elements.html", {'passentry': zip(passentry,passentrycount,all_pass),#ersale 2 loop be html
                                             },
                 ) #en value dar html call mishavad.
    del all_pass


# def editpass(request):
#      form = forms.ChangePassword()
#      if request.method == 'POST':
#          form = forms.ChangePassword(request.POST)
#         if form.is_valid():#true or false
#             oldpass = request.POST["old_pass"]
#             newpas1 = request.POST["new_pass1"]
#             newpas2 = request.POST["new_pass2"]
#             # if oldpass == '' or newpas1=='' or newpas2=='':
#             #     messages.error(request, 'Plz provide the value for fields')
#             #     return redirect("/page/elements")
#             passentry = PassEntry.objects.filter(user_id_id=11).values() #uid
#             # if newpas1 != newpas2:
#             #     messages.error(request, 'Passwords mismatch.')
#             #     return redirect("/page/elements")
#             # else:
#             #     for i in passentry:
#             #         i = i['id']
#             #         getoldpas=PassEntry.objects.get(id=i).pass_word#return one record
#             #         checkoldpas = check_password(oldpass, getoldpas)
#             #         if (checkoldpas is True):
#             #             hashnewpas1 = make_password(newpas1, hasher='argon2')
#             #             pasupdate = PassEntry.objects.update(Pass_word=hashnewpas1)
#             #             messages.success(request,'Password changed successfully')
#             #             break
#             #         if checkoldpas is False:
#             #                messages.error(request, 'Please enter the correct old password.')
#             #                break
#         else:
#             messages.error(request,"Plz correct the error")
#     else:#GET
#         form = forms.ChangePassword()
#         messages.info(request,'Welcome for first time')
#      return render(request, 'editpass.html', {'form': form})


###############################################################################################################
#class based view for modal
class PassModalForm(BSModalFormView):
    template_name = '/editpass.html'
    form_class = ChangePassword
    sucess_message= 'ok its done'
    success_url = reverse_lazy('elements')




























def contact1(request):  # view ke motasel b file html ast..
    if request.method == 'POST':  # zamani ke karbar page ra view mikonad(GET) false ast.
        myform = ContactForm(request.POST)
        if myform.is_valid():
            cd = myform.cleaned_data  # en attribute yek dict as datahaye submit shode ast.
            # send_mail(cd['subject'],#func ersale email-subject,matn va adress ferestande
            #     cd['message'],
            #    cd.get('email', 'noreply@example.com'),
            #    ['siteowner@example.com'],)#listi as girandegan email
            return HttpResponseRedirect('/contact1/thanks')  # baad aa ersale email redirect mishavad.
    else:
        myform = ContactForm(initial={
            'subject': 'i love your site'})  # hamannade class datetime dar bala/initial=meqdare pishfarz dar subject
    return render(request, 'myviews.html', {'myform': myform})  # negareshe digri az render dar func bala.

# request.POST.get('subject',''): #agar az request.post[] estefadeh mishod dar soorate nabood value error midad vali dar en soorat argomane dovom value pishfarz ast.
