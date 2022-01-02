from django.urls import path


from . import views

urlpatterns = [
  path('', views.index, name='accountindex'),
  # signup はデフォルトで用意されていないため
  path('signup/', views.SignUpView.as_view(), name='signup'),
  path('edit/', views.EditView.as_view(), name='accountedit'),
]