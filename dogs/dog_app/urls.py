from django.urls import path
from . import views
from django.contrib.auth.views import login, logout


urlpatterns = [
    path('',views.user, name='user'),
    path('register',views.register,name='register'),
    path('login',views.auth_login,name='auth_login'),
    path('index',views.index, name='index'),
    path('lout',views.Lout,name='lout'),
    path('create/',views.create),
    path('edit/<int:dog_id>', views.edit),
    path('edit/update/<int:dog_id>', views.update),
    path('delete/<int:dog_id>', views.delete),
]



