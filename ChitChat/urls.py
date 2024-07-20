from django.urls import path, include
from ChitChat import views as chat_views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),
    path("auth/login/", LoginView.as_view(template_name="chat/login.html"), name="login-user"),
    path("auth/logout/", chat_views.logoutView, name="logout-user"),
]