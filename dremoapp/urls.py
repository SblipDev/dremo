"""dremoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
from dremo.views import IndexView, signup, AccountActivationSentView, activate
# from users.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('dremo.api.urls')),
    path('', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('account_activation_sent/', AccountActivationSentView.as_view(), name='account_activation_sent'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    # path('api/user/info/status', main),
    path('', IndexView.as_view(), name='home')
]
