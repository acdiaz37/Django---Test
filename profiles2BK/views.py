from django.views.generic.list import ListView
from registration.models import Profile

# Create your views here.

class ProfileListView (ListView):
    model = Profile
    template_name = "profiles/profile_list.html"

    
