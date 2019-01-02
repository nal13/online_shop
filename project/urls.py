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

from accounts import views as a_views
from shop import views as s_views

urlpatterns = [

    # authentication app
    path('signup/', a_views.signup, name='signup'),
    path('login/', a_views.login, name='login'),

    # shop app
    path('', s_views.home, name='home'),

    re_path('list_categoria/(?P<categoria>\w+)/', s_views.list_categoria, name='list_categoria'),
    re_path('get_modelo/(?P<id>\d+)/', s_views.get_modelo, name='get_modelo'),
    re_path('add_modelo/(?P<type>\w+)/', s_views.add_modelo, name='add_modelo'),
    re_path('remove_modelo/(?P<id>\d+)/', s_views.remove_modelo, name='remove_modelo'),
    re_path('edit_modelo/(?P<id>\d+)/', s_views.edit_modelo, name='edit_modelo'),

    re_path('get_loja/(?P<id>\d+)/', s_views.get_loja, name='get_loja'),
    path('add_loja/', s_views.add_loja, name='add_loja'),
    re_path('remove_loja/(?P<id>\d+)/', s_views.remove_loja, name='remove_loja'),
    re_path('edit_loja/(?P<id>\d+)/', s_views.edit_loja, name='edit_loja'),

    path('admin/', admin.site.urls),
    # path('favicon.ico', RedirectView.as_view(url='/static/shop/css/ajax-loader.gif')),
]
