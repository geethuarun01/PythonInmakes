from django.shortcuts import render

from travelapp.models import Place, People


# Create your views here.
def home(request):
    obj= Place.objects.all()
    obj1=People.objects.all()

    return render(request,"index.html",{'result':obj, 'result1':obj1})

