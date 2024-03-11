from django.shortcuts import render

# Create your views here.

from app.forms import userform

from django.http import HttpResponse
def register(request):
    uf = userform()

    if request.method == 'POST':
        ud = userform(request.POST)

        if ud.is_valid():
            
            
            
            # ud.cleaned_data['name']




            return HttpResponse('data is valid')

        else:

            return HttpResponse("data is not valid")





    return render(request,'register.html',{'uf':uf})




