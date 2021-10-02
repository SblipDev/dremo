from django.views.generic import TemplateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

class IndexView(TemplateView):
    template_name = 'dremo/index-dev.html'


from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'dremo/signup.html', {'form': form})