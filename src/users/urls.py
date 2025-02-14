from django.urls import path

from .views import RegisterView, CustomLoginView, logout_view, my_account_view

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('my_account/', my_account_view, name='my_account'),
    path('logout/', logout_view, name='logout')
]

