from django.shortcuts import render, get_list_or_404, get_object_or_404

from .models import Vanished, Story, Point


def index(request):
    mmiw = Vanished.objects.all()
    context = {'mmiw': mmiw}
    return render(request, 'cases/index.html', context)


def detail(request, id):
    victim = get_object_or_404(Vanished, id=id)
    related_articles = Story.objects.filter(vanished__first_name=victim.first_name)
    markers = Point.objects.filter(vanished__first_name=victim.first_name)
    return render(request, 'cases/detail.html', {'victim': victim, 'articles':related_articles, 'markers':markers })


def classification_select(request, ctype):
    victim_type = get_list_or_404(Vanished, classification=ctype)
