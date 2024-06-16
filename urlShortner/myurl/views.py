from django.shortcuts import redirect, render
import uuid
from .models import Url
from django.http import HttpResponse, JsonResponse
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
    
def goto(request,uid):
   myurl = Url.objects.get(uid=uid)
   return redirect(myurl.my_Url)

def fetchlink(request):
   data={}
   myurl = Url.objects.all()
   data = {
      'myurl':list(myurl.values())
   }
   return JsonResponse(data)