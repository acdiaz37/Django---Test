from django.urls import path
from .views import ProfileListView


profile_patterns = ([
    path('', ProfileListView.as_view(), name='list'), 
], 'profiles')