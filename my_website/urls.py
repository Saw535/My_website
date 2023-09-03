from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from quotes import views


urlpatterns = [
    path('', views.home, name='home'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls),
    path('profile/', views.profile, name='profile'),
]