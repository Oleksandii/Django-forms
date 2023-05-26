from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse





class NewUser(forms.Form):
    name = forms.CharField(label='Name')
    surname = forms.CharField(label='Surname')
    department= forms.CharField(label='Department',max_length=4)

def index(request):
    if 'names' not in request.session:
        request.session['names']= []
        request.session['surnames']=[]
        request.session['departments']=[]

    return render(request,'users/index.html',{"names":request.session['names'],"surnames":request.session['names'],"departments":request.session['departments']})


def add(request):
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            request.session['names']+=[name]
            surname= form.cleaned_data['surname']
            request.session['surnames']+=[surname]
            department = form.cleaned_data['department']
            request.session['departments']+=[department]
            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request,'users/add.html',{'form': form} )

    return render(request,'users/add.html',{'form':NewUser()})
# Create your views here.
