from django.shortcuts import render, HttpResponse
from rakun_elastic.document import TestPersonnelDocument
from elasticsearch_dsl.query import Q

# Create your views here.

def index(request):
    try:
        if request.COOKIES.get('doc_id'):
            query_object = TestPersonnelDocument.search().filter('ids', values=request.COOKIES.get('doc_id'))
            query = query_object.execute()
            for per_data in query:
                per_data
            context = {
                'id': request.COOKIES.get('doc_id'),
                'company': per_data.company,
                'user_name': per_data.user_name,
                'user_surname': per_data.user_surname,
                'phone_number': per_data.phone_number,
            }
        else:
            status = "COOKIE VYOK"
            context = {
                'status': status,
            }
        return render(request, 'rakun/layout.html', context)
    except Exception:
        print('hata')