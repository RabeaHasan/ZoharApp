from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.template import loader

from zohar_app.forms import SurveyForm  
from zohar_app.models import Survey 

def index(request):
    template = loader.get_template('page2.html')
    return HttpResponse(template.render())

 

# Create your views here.  
def servey(request):  
    if request.method == "POST":  
        form = SurveyForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = SurveyForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    Surveys = Survey.objects.all()  
    return render(request,"show.html",{'Surveys':Surveys})  
def edit(request, barcode):  
    survey = Survey.objects.get(barcode=barcode)
    return render(request,'edit.html', {'Survey':survey})  
def update(request, barcode): 
    survey = Survey.objects.get(barcode=barcode)  
    form = SurveyForm(request.POST, instance = survey)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'Survey': survey})  
def destroy(request, id):  
    survey = Survey.objects.get(id=id)  
    survey.delete()  
    return redirect("/show")  