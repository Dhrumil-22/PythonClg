from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup(request):
    template_data = {'title':'Signup',
                     'form':UserCreationForm}
    if request.method == 'GET' :
        return render(request,'signup.html',{'template_data':template_data})
    elif request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else : 
            template_data['form'] = form
            return render(request,'signup.html',{'template_data':template_data})
            