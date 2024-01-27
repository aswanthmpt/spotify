from django.urls import path
from . import views
app_name='auth'
urlpatterns = [
    path('usersignin',views.signin,name='signin'),
    path('userlogin',views.login,name='login'),
    path('userlogout',views.logout,name='logout')
]
