from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.template import loader
from numpy import true_divide

from zohar_app.forms import SurveyForm  
from zohar_app.models import Survey 
from zohar_app.models import Statuses
from zohar_app.models import Manufacturer

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
def statuses(request):
    statuses = Statuses.objects.all()  
    return render(request,"Statuses table.html",{'statuses':statuses, 'failed':False})  
def manufacturers(request):
    manufacturers = Manufacturer.objects.all()  
    return render(request,"manufacturer.html",{'manufacturers':manufacturers, 'failed':False})  
def edit(request, id):  
    survey = Survey.objects.get(id=id)
    return render(request,'edit.html', {'Survey':survey, 'failed':False})  
def update(request, id): 
    survey = Survey.objects.get(id=id)  
    form = SurveyForm(instance = survey)
    if request.method == 'POST':
        form = SurveyForm(request.POST, instance = survey)  
        if form.is_valid():  
            form.save()  
            return redirect("../show") 
    return render(request, 'edit.html', {'Survey': survey , 'failed':True})  

def destroy(request, id):  
    survey = Survey.objects.get(id=id)  
    survey.delete()  
    return redirect("../show")  

    
#  blogs = Blog.objects.get(id=pk)
#     form = BlogForm(instance=blogs)

#     if request.method == 'POST':
#         form = BlogForm(request.POST, instance=blogs)
#         if form.is_valid():
#             form.save()
#             return redirect('/search')

#     context = {
#         'blogs': blogs,
#         'form': form,
#     }
#     return render(request,'update.html',context)