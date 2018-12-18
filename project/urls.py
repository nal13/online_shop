"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from shop import views
from accounts import views as accounts_views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/', views.product, name='product'),
    path('store/', views.store, name='store'),

    re_path('filter_categoria/(?P<categoria>\w+)/', views.filter_categoria, name='filter_categoria'),

    path('add_buttons/', views.add_buttons, name='add_buttons'),
    path('list_modelo/', views.list_modelo, name='list_modelo'),
    re_path('get_modelo/(?P<id>\d+)/', views.get_modelo, name='get_modelo'),
    re_path('add_modelo/(?P<type>\w+)/', views.add_modelo, name='add_modelo'),
    re_path('remove_modelo/(?P<id>\d+)/', views.remove_modelo, name='remove_modelo'),
    re_path('edit_modelo/(?P<id>\d+)/', views.edit_modelo, name='edit_modelo'),

    re_path('get_loja/(?P<id>\d+)/', views.get_loja, name='get_loja'),
    path('add_loja/', views.add_loja, name='add_loja'),
    re_path('remove_loja/(?P<id>\d+)/', views.remove_loja, name='remove_loja'),
    re_path('edit_loja/(?P<id>\d+)/', views.edit_loja, name='edit_loja'),

    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', accounts_views.login, name='login'),

    #https://stackoverflow.com/questions/9371378/warning-not-found-favicon-ico
    #in accounts, its already implemented
    path('favicon.ico', RedirectView.as_view(url='/static/shop/css/ajax-loader.gif')),
    path('admin/', admin.site.urls),
]
