from django.conf.urls import url
from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    # re_path('Login$', views.LoginView.as_view(),name = 'Login'),
]