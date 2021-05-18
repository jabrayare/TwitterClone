from django.urls import path
from . import views

urlpatterns = [
    path('following', views.following, name='following'),
    path('followers', views.followers, name='followers'),
    path('individualFollowing/<int:id>', views.individual_following,
         name='individualFollowing'),
    path('individualFollowers/<int:id>', views.individual_followers,
         name='individualFollowers'),
]
