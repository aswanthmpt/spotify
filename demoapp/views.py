from django.shortcuts import render
from . models import Data

# Create your views here.
def home(req):
    data=Data.objects.all()
    return render(req,'index.html',{"data":data})
