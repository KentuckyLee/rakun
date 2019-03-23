from django.shortcuts import render, HttpResponse
from rakun_elastic.document import TestPersonnelDocument
from elasticsearch_dsl.query import Q
from Context.ContextView import Authantication

# Create your views here.

def index(request):
    try:
        context = Authantication.getInstance().getUser()
        print('.........CONTEXT..................', context)
        return render(request, 'rakun/layout.html', context)
    except Exception:
        print('hata')