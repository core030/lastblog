from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Twoblog


def twohome(request):
    twoblogs = Twoblog.objects
    return render(request, 'twohome.html', {'twoblogs':twoblogs})

def twodetail(request, twoblog_id):
    twodetails = get_object_or_404(Twoblog, pk=twoblog_id)
    return render(request, 'twodetail.html', {'twodetails':twodetails})

def twonew(request):
    return render(request, 'twonew.html')

def twocreate(request):
    twoblog = Twoblog()
    twoblog.title = request.GET['title']
    twoblog.body = request.GET['body']
   # blog.image = request.GET['image']
    twoblog.pub_date = timezone.datetime.now()
    twoblog.save()
    return redirect('/blogapp/'+str(twoblog.id))




# Create your views here.
