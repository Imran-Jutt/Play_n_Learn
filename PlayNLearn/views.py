from django.shortcuts import render
from PlayNLearn.forms import signUpForm


def signUp(request):
    if(request.method=='POST'):
        form=signUpForm(request.POST or None)
        if(form.is_valid()):
            signUp_item=form.save(commit=False)
            signUp_item.save()
    else:
        form=signUpForm()
    return render(request,'PlayNLearn/signUp.html',{'form':form})
def home(request):
    if(request.method=='POST'):
        form = signUpForm(request.POST or None)
        if (form.is_valid()):
            signUp_item = form.save(commit=False)
            signUp_item.save()
        name=request.POST['U_Name']
        context={
            'uname': name
    }
        return render(request, 'PlayNLearn/home.html', context)
    else:
        context={
            'uname':"Null"
        }
        return render(request, 'PlayNLearn/home.html',context)
def landingPage(request):

        return render(request, 'PlayNLearn/index.html')