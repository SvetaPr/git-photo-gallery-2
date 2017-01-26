from django.conf.urls import url

from authorization import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^register/', views.register),
]
