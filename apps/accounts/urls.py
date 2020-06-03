from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from .views import SignupView

app_name = 'accounts'
urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
