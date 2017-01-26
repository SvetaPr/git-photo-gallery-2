from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from photo import views

urlpatterns = [
    url(r'^photos/$', views.all_photos),
    url(r'^photos/(?P<user_id>\d+)/$', views.photos),
    url(r'^photos/addphoto/$', views.add_photo),
    url(r'^photo/(?P<photo_id>\d+)/$', views.photo),
    # url(r'^', views.photos),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)