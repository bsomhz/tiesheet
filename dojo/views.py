from django.shortcuts import render
from django.views.generic import ListView
from dojo.models import Dojo, Operator, Player


# Create your views here.


class DojoListView(ListView):
    queryset = Dojo.objects.all()
    context_object_name = 'dojos'
    template_name = 'dojo/dojo.html'


# def index(request):
#     return render(request, 'dojo/index.html')
