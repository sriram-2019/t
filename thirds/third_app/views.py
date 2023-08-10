from django.shortcuts import render
from django.http import HttpResponse
from . import forms
import populate
# Create your views here.
def index(request):
    return render(request,"index.html")
def ct(request):
    form=forms.formname()
    if(request.method=="POST"):
        form=forms.formname(request.POST)
        if form.is_valid():
            data1=form.cleaned_data['name']
            data2=form.cleaned_data['email']
            data3=(request.POST.get("password"))
            populate.insert(data1,data2,data3)
    return render(request,"ctm.html")