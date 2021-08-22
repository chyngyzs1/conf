from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('login/', views.loginPage, name='login_page'),
    path('register/', views.registerPage, name='register_page'),
    path('logout/', views.logoutUser, name='logout_page'),
    path('sendform/', views.sendform, name='sendform_page'),
    path('user_room/', views.user_room, name='user_room'),
    path('update_form/<int:pk>', views.update_form, name='update_form'),
    path('delete_form/<int:pk>', views.delete_form, name='delete_form'),
    path('committee/', views.committee, name='committee_page'),
    path('speakers/', views.speakers, name='speakers_page'),
    path('abstracttemplate/', views.abstempl, name='abstempl_page'),
    path('importantdate/', views.impdate, name='impdate_page'),
    path('topics/', views.conftopic, name='conftopic_page'),
    path('participiants/', views.particip, name='particip_page'),
    path('proceedings/', views.proceeding, name='proceeding_page'),
    path('aboutKyrgyzstan/', views.kyrgyzstan, name='kyrgyzstan_page'),
    path('historyOfMadea/', views.history_madea, name='history_madea_page'),
    path('gallery/', views.gallery, name='gallery_page'),
    path('contacts/', views.contacts, name='contacts_page'),

]