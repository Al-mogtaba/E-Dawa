from django.shortcuts import render, redirect 
from django.contrib import messages
from django.views import View
from .forms import RegisterForm


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'main/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'تم إنشاء حسابك بنجاح {username}')

            return redirect('login')

        return render(request, self.template_name, {'form': form})


