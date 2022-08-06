from django.urls import path, include
from .views import idea_owner, company, investor, findInv

app_name = 'custom_auth'

urlpatterns = [
    # path('', include('findApp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', findInv.SignUpView.as_view(), name='signup'),
    path('accounts/signup/IdeaOwner/', idea_owner.IdeaOwnerSignUpView.as_view(), name='idea_owner_signup'),
    path('accounts/signup/Investor/', investor.InvestorSignUpView.as_view(), name='investor_signup'),
    path('accounts/signup/Company/', company.CompanySignUpView.as_view(), name='company_signup'),
    # path('', idea_owner.Dashboard, name='dashboard'),
    # path('login/', idea_owner.LoginView.as_view(), name='login'),
    # path('logout/', views.Logout, name='logout'),
]