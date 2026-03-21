"""
URL configuration for Jango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from .views import *
from Receipe.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homeview,name = "Home"),
    path('Login/',Login_page, name = "Login"),
    path('Logout/',logout_page, name = "Logout"),
    path('Register/',Register_page, name = "Register"),
    path('Menu/',Viewmenu, name = "Menu"),
    path('Receipe/',receipe, name = "Receipe"),
    path('View_Receipe/',View_receipe, name = "View_Receipe"),
    path('delete_receipe/<id>/', delete_receipe, name='delete_receipe'),
    path('update_receipe/<id>/', update_receipe, name='update_receipe'),

]
#this below has to be written to workon files or show fles in development mode
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns() 