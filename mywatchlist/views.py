from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList

# Create your views here.
def show_watchlist(request):
    my_watch_lists = MyWatchList.objects.all()
    
    watched = MyWatchList.objects.filter(watched=True).count()
    unwatched = MyWatchList.objects.filter(watched=False).count()
    pesan=''
    
    if watched >= unwatched:
        pesan = 'Selamat, kamu sudah banyak menonton!'
    else:
        pesan = 'Wah, kamu masih sedikit menonton!'

    context = {
        'my_watch_lists': my_watch_lists,
        'pesan': pesan,
        'name': 'Christopher Nathanael Wijaya',
        'student_id': '2106630044',
    }
    return render(request, 'watchlist.html', context)

def show_json(request):
    my_watch_lists = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('json', my_watch_lists), content_type='application/json')

def show_xml(request):
    my_watch_lists = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize('xml', my_watch_lists), content_type='application/xml')

