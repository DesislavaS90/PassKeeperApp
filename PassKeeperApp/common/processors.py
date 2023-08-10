import random
from PassKeeperApp.common.models import Facts, Advices, Fun


def facts_and_advice(request):

    start = 1
    stop = 10

    current_fact = Facts.objects.get(id=random.randint(start, stop))
    current_advice = Advices.objects.get(id=random.randint(start, stop))
    current_fun = Fun.objects.get(id=random.randint(start, stop))

    context = {
        'current_fact': current_fact,
        'current_advice': current_advice,
        'current_fun': current_fun
    }

    return context