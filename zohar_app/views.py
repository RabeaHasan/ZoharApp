from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.template import loader
from numpy import true_divide

from zohar_app.forms import SurveyForm  
from zohar_app.models import survey 
from zohar_app.models import statuses
from zohar_app.models import manufacturers
from zohar_app.models import mainsites
from zohar_app.models import mainitems
from zohar_app.models import items

def index(request):
    template = loader.get_template('page2.html')
    return HttpResponse(template.render())

 

# Create your views here.  
def Survey(request):  
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
    surveys = survey.objects.all()
    return render(request,"show.html",{'surveys':surveys})  
def show_statuses(request):
    Statuses = statuses.objects.all()
    return render(request,"Statuses table.html",{'statuses':Statuses, 'failed':False})  
def show_manufacturers(request):
    Manufacturers = manufacturers.objects.all()  
    return render(request,"manufacturer.html",{'manufacturers':Manufacturers, 'failed':False}) 
def show_mainsites(request):
    Mainsites = mainsites.objects.all()  
    return render(request,"mainsites.html",{'mainsites':Mainsites, 'failed':False}) 
def show_mainitems(request):  
    Mainitems = mainitems.objects.all()  
    return render(request,"mainitems.html",{'mainitems':Mainitems, 'failed':False})  
def show_items(request):
    Items = items.objects.all()  
    return render(request,"items.html",{'items1':Items, 'failed':False}) 
def edit(request, ID):  
    survey = Survey.objects.get(ID=ID)
    return render(request,'edit.html', {'Survey':survey, 'failed':False})  
def update(request, ID): 
    survey = Survey.objects.get(ID=ID)  
    form = SurveyForm(instance = survey)
    if request.method == 'POST':
        form = SurveyForm(request.POST, instance = survey)  
        if form.is_valid():  
            form.save()  
            return redirect("../show") 
    return render(request, 'edit.html', {'Survey': survey , 'failed':True})  

def destroy(request, ID):  
    survey = Survey.objects.get(ID=ID)  
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