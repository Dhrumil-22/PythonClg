from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'home/index.html')

def about(request):
    data  = {"name":['ABC','XYZ','PQR'],'id':5}
    return render(request,'home/about.html',{'d':data})
