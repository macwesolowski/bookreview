from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse


class RegisterView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('my_account')
        register_form = RegistrationForm()
        return render(request, 'views/register.html', {'register_form': register_form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('my_account')
        register_form = RegistrationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)
            messages.success(request, f'Użytkownik {user.username} został poprawnie zarejestrowany.')
            return redirect('my_account')
        else:
            messages.error(request, f'Wystąpił błąd podczas próby rejestracji.')
            return render(request, 'views/register.html', {'register_form': register_form})


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'views/login.html'

    def get_success_message(self, cleaned_data):
        return f"Jesteś zalogowany jako {self.request.user.username}"

    def form_invalid(self, form):
        messages.error(self.request, "Wystąpił błąd podczas logowania.")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('my_account')


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')


@login_required
def my_account_view(request):
    return render(request, 'views/my_account.html')

