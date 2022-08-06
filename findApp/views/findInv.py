from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def home(request):
    if request.user.is_authenticated:
        if request.user.is_idea_owner:
            return redirect('idea_owner:quiz_change_list')
        elif request.user.is_investor:
            return redirect('investor:quiz_change_list')
        elif request.user.is_company:
            return redirect('investor:quiz_change_list')
        else:
            return redirect('idea_owner:quiz_list')
    return render(request, 'findApp/home.html')