from django.shortcuts import render
import uuid
from .models import Url
from django.http import HttpResponse
# Create your views here.
def urlshort(request):
    data={}
    
    return render(request,'index.html',data)

def createUrl(request):
    if request.method=="POST":
      url = request.POST.get('url')
      uid = str(uuid.uuid5(uuid.NAMESPACE_URL, url))[:5]
      myurl = Url.objects.create(my_Url=url,uid=uid)
      myurl.save()
      return HttpResponse(uid)