from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# 自分で定義したもの
from .models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.

# 
def index(request):
  return render(request, 'registration/login.html')

# アカウント作成
class SignUpView(CreateView):
  model = User
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'

# アカウント情報編集
@method_decorator(login_required, name='dispatch')
class EditView(LoginRequiredMixin, UpdateView):
  model = User
  form_class = CustomUserChangeForm
  template_name = 'registration/edit.html'
  success_url = reverse_lazy('index')

  def get_object(self):
    return self.request.user