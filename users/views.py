import secrets
from django.contrib.auth.mixins import LoginRequiredMixin
from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from services.functions.get_random_number import get_random_number
from users.forms import UserRegisterForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, TemplateView
from users.models import User
from users.forms import UserProfileForm, RecoverPasswordForm

# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = "Перейдите на почту для подтверждения..."

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}/'
        send_mail(
            'Подтверждение почты',
            f'Перейдите по ссылке для подтверждения почты {url}',
            EMAIL_HOST_USER,
            [user.email],
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        user_ = User.objects.get(email=self.request.user.email)
        profile = form.save()
        if profile.avatar != user_.avatar:
            user_.avatar.delete(False)
        return super().form_valid(form)


def recovery_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        new_password = get_random_number()
        send_mail(
            "Восстановление доступа",
            f"Ваш новый пароль : {new_password}",
            EMAIL_HOST_USER,
            [user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse("users:login"))
    else:
        form = RecoverPasswordForm
        context = {"form": form}
        return render(request, "users/recovery_password_form.html", context)