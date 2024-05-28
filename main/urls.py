from django.urls import path
from .views import register, login_view, home, logout_view, create_news, view_news

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home, name='home'),
    path('create_news/', create_news, name='create_news'),
    path('view_news/', view_news, name='view_news'),
]
