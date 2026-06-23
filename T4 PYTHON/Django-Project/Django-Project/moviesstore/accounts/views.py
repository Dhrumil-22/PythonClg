from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login as auth_login


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
        
        
def login(request):
    template_data = {'title':'login'}
    if request.method=='GET':
        return render(request, 'signup.html', {'template_data':template_data})
    elif request.method=='POST':
        user = authenticate(request,
                            username = request.POST['username'],
                            password = request.Post['password'])
        if user is None:
            template_data['error']='The user or password is incorrect'
            return render(request, 'signup.html', {'template_data':template_data})
        else:
            auth_login(request,user)
            return redirect('home')       
        
        
            