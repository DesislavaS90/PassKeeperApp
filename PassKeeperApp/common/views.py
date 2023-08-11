from django.shortcuts import render
from PassKeeperApp.password_generator.forms import PasswordGeneratorForm


def index(request):
    form = PasswordGeneratorForm()

    return render(request, 'index.html', {'form': form})


def page_404(request):
    return render(request, 'index.html')
