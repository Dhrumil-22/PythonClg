from django.shortcuts import render

# Create your views here.
def home(request):
    template_data = {'title':'Movies Store'}
    return render(request,'home.html',{'template_data':template_data})

def about(request):
    data = {'Name':['ABC','XYZ','PQR'],'ID':1}
    return render(request,'about.html',{'data':data})
