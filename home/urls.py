from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/', views.index, name="index"),
    url(r'^about/', views.about, name="about"),
    url(r'^alumni/', views.alumni, name="alumni"),
    url(r'^download/', views.download, name="download"),
    url(r'^notice/', views.notice, name="notice"),
    url(r'^profiles/', views.profiles, name="profiles"),
    url(r'^recruiters/', views.recruiters, name="recruiters"),
    url(r'^whyus/', views.whyus, name="whyus"),
    url(r'^tnp_team/', views.team, name="tnp_team"),
    url(r'^gallery/',views.gallery, name="gallery"),
]