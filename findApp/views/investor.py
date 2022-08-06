from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView, CreateView
from ..models import CustomUser
from .. import forms

# Create your views here.

class InvestorSignUpView(CreateView):
    """sign up user view"""
    
    model = CustomUser
    form_class = forms.InvestorSignUpForm
    success_url = reverse_lazy('findApp:dashboard')
    template_name = 'registration/signup-form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'investor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        """ process user signup"""
        user = form.save(commit=False)
        user.save()
        login(self.request, user)
        if user is not None:
            return HttpResponseRedirect(self.success_url)

        return super().form_valid(form)

def Dashboard(request):
    """ make dashboard view """
    return render(request, 'dashboard.html')

class LoginView(FormView):
    """login view"""
    
    form_class = forms.LoginForm
    success_url = reverse_lazy('findApp:dashboard')
    template_name = 'authentication/login.html'
    
    
    def form_valid(self, form):
        """processes users' login"""
        credentials = form.cleaned_data
        
        user = authenticate(username=credentials['email'],
                            password=credentials['password'])

        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(self.success_url)
        
        else:
            messages.add_message(self.request, messages.INFO, 'Wrong credentials\
                                please try again')
            return HttpResponseRedirect(reverse_lazy('templates.registration:login'))
