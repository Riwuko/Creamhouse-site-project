from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


class SignUp(FormView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('cosmetics:home')

    def form_valid(self, form):
        form.save()
        self.login_user(form)
        return super().form_valid(form)

    def login_user(self, form):
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
