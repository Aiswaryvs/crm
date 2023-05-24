from django.contrib import admin
from django.urls import path,include
from app.user_authentication import views

urlpatterns = [
    path('user/register',views.UserRegistrationView.as_view()),
    # path('user/<int:id>',views.UserDetailView.as_view()),
    

]
