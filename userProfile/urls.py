from django.urls import path
from . import views

urlpatterns = [
    path('create_profile', views.create_profile, name='create_profile'),
    path('edit_profile', views.editProfile, name='edit_profile'),
    path('userprofile', views.userProfile, name='userprofile'),
    path('individualprofile/<int:id>', views.individual_profile_page,
         name='individualprofile'),
    path('userprofile_accounts', views.userProfile_accounts,
         name='userprofile_accounts'),
]
