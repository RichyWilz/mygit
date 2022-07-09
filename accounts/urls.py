from unicodedata import name
from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns =[ 
    path('',views.login_user, name="login"),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    ]
    
    
