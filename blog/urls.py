from django.urls import path
from .views import *
urlpatterns = [
    path('computers/', computers, name="computers"),
    path('contact/',  contact,   name="contact"),
    path('',    index,     name="index"),
    path('mans_clothes/', mans_clothes,  name="mans_clothes"),
    path('womans_clothes/', womans_clothes, name="womans_clothes"),
    path('komputer/<slug:komputer>', komputerDetail, name='komputerDetail'),
    path('watch/<slug:watch>/', watchDetail, name='watchDetail'),
    path('koylak/<slug:koylak>/', koylakDetail, name='koylakDetail'),
    path('womanfor/<slug:womanfor>/', womanforDetail, name='womanforDetail'),
    path('small/<slug:small>/', smallDetail, name='smallDetail'),
    path('koylak/delete/<slug>/', KoylakDeleteView.as_view(), name='koylak_delete'),
    path('koylak/edit/<slug>/', KoylakUpdateView.as_view(), name='koylak_edit'),
    path('koylak_create/', KoylakView.as_view(), name="koylak_create")
]