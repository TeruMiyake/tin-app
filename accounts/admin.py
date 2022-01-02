from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# Register your models here.


# がっつり表示をいじりたい場合、fieldsets を一から定義するしかない（UserAdmin に書かれちゃってるから）
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username','displayname','tmptime','tmpmiss', 'tmpevidenceurl', 'tmpuserurl']
    list_display_links = ['username',]
    list_editable = ['displayname', 'tmptime', 'tmpmiss', 'tmpevidenceurl', 'tmpuserurl']


admin.site.register(User, CustomUserAdmin)