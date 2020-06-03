from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, logout
from django.views.generic import CreateView
from .forms import SignupForm

# Create your views here.
class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        logout(self.request) #? to logout the logged in user if a new user is to signup
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Signup"
        return context

