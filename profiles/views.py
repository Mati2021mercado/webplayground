from django.shortcuts import render, get_list_or_404
from registration.models import Profile
# Create your views here.
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"
    paginate_by = 3

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"
    
    
    def get_object(self):
        return get_list_or_404(Profile,user__username=self.kwargs['username'])