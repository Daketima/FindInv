from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (CustomUser, Idea, IdeaOwner, Investor, Company)

# Register your models here.

class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = ('email', 'is_staff', 'is_active', 'is_idea_owner', 'is_investor', 'is_company')
    list_filter = ('email', 'is_staff', 'is_active', 'is_idea_owner', 'is_investor', 'is_company')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'is_idea_owner', 
                       'is_investor', 'is_company')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Idea)
admin.site.register(IdeaOwner)
admin.site.register(Investor)
admin.site.register(Company)


# from django.apps import apps


# models = apps.get_models()

# for model in models:
#     admin.site.register(model)