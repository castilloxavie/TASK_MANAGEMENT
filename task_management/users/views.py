from django.views.generic import UpdateView
from .models import Profile
from .forms import UserProfileForm

class UserProfileUpdateView(UpdateView):
    model = Profile
    form_class = UserProfileForm
    template_name = 'user_profile/user_profile_form.html'
    success_url = '/profile/'
