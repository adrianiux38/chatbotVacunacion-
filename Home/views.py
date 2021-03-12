from django.shortcuts import render
from .models import RegistrosVacunacion
# Create your views here.


# Create your views here.

def home(request):
	registro=RegistrosVacunacion.objects.all() # Collect all records from table 
	return render(request,'home/home.html',{'registro':registro})


    