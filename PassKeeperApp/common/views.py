from django.shortcuts import render
from PassKeeperApp.common.models import Facts, Advices, Fun
from PassKeeperApp.password_generator.forms import PasswordGeneratorForm
import random


def index(request):
    form = PasswordGeneratorForm()

    start = 1
    stop = 10

    current_fact = Facts.objects.get(id=random.randint(start, stop))
    current_advice = Advices.objects.get(id=random.randint(start, stop))
    current_fun = Fun.objects.get(id=random.randint(start, stop))

    context = {
        'form': form,
        'current_fact': current_fact,
        'current_advice': current_advice,
        'current_fun': current_fun
    }

    return render(request, 'index.html', context)










