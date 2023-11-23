from django.shortcuts import render
from django.http import HttpResponseRedirect
from .cat import Cat


# Create your views here.
def main_view(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        return HttpResponseRedirect('cat_page.html/')


def cat_view(request):
    if Cat.name:
        pass
    else:
        Cat.get_name(request)

    if request.method == 'POST':
        if request.POST.get('select') == "play":
            Cat.play()
        elif request.POST.get('select') == "feed":
            Cat.feed()
        elif request.POST.get('select') == "sleep":
            Cat.asleep()
        else:
            pass

    context = {
        'name': Cat.name,
        'age': Cat.age,
        'happiness': Cat.happiness,
        'hunger': Cat.hunger,
    }

    return render(request, 'cat_page.html', context)




