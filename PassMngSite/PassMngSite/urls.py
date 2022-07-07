"""PassMngSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#from PassMngSite import myviewscontroller
from . import myviewscontroller
urlpatterns = [
    path('registerlogin/', myviewscontroller.registerlogin, name= 'registerlogin'), #button register dar index
    path('registerlogin/register', myviewscontroller.register, name= 'register'), # func register dar action form va viewcontroller
    path('registerlogin/login', myviewscontroller.login, name='login'),
    path('page/about/', myviewscontroller.about, name='about'),
    path('page/services/', myviewscontroller.services, name='services'),
    path('page/contact/', myviewscontroller.contact, name='contact'),
    path('page/blog/', myviewscontroller.blog, name='blog'),
    path('page/elements/', myviewscontroller.elements, name='elements'),
    path('page/blog/single-blog/', myviewscontroller.singleblog, name='singleblog'),
    path('logout/', myviewscontroller.logout, name='logout'), #chon dar view index taarif shode.
    path('passentry/', myviewscontroller.passentry, name='passentry'),
    path('passentry/passentrysubmit', myviewscontroller.passentrysubmit, name= 'passentrysubmit'),#submit data button
    path('admin/', admin.site.urls), # hatman ba slash-- tak page ha hatman ba slash
    path('', myviewscontroller.index, name='index'), #homepage
    path('editpass/', myviewscontroller.PassModalForm.as_view(), name='editpass'),  # changepassword/class based_view as view

] #a list

#urlpatterns1 = {
 #   path('register', myviewscontroller.register, name='register'),
#}
