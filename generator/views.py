from django.shortcuts import render
import random
# Create your views here.


def home(request):
    return render(request, 'generator/home.html', )


def password(request):
    the_password = ''
    prealph = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    alph = ''
    if request.GET.get('uppercase'):
        prealph += (prealph.upper())
    print(prealph)
    if request.GET.get('numbers'):
        prealph += '1,2,3,4,5,6,7,8,9,0'
    if request.GET.get('special'):
        prealph += '!,@,#,$,%,^,&,*,(,),_,-,+,=,|'
    alph = list(prealph.split(','))
    lenOfPassword = int(request.GET.get('length'))
    for i in range(lenOfPassword):
        the_password += str(random.choice(alph,))

    return render(request, 'generator/pass.html', {'password': the_password})
