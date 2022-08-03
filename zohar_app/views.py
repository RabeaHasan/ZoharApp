from pyexpat import model
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.template import loader
from numpy import true_divide

from zohar_app.forms import SurveyForm  
from zohar_app.models import Survey 
from zohar_app.models import Statuses
from zohar_app.models import Manufacturers
from zohar_app.models import Mainsites
from zohar_app.models import Mainitems
from zohar_app.models import Items
from zohar_app.models import Guides

def index(request):
    template = loader.get_template('page2.html')
    return HttpResponse(template.render())
    
# Create your views here.
def main(request):
    return render(request,"Main.html")  
def survey(request):  
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
    surveys = Survey.objects.all()
    return render(request,"show.html",{'surveys':surveys})  
def show_statuses(request):
    statuses = Statuses.objects.all()
    return render(request,"Statuses table.html",{'statuses':statuses,})  
def show_manufacturers(request):
    manufacturers = Manufacturers.objects.all()  
    return render(request,"manufacturer.html",{'manufacturers':manufacturers,}) 
def show_mainsites(request):
    mainsites = Mainsites.objects.all()  
    return render(request,"mainsites.html",{'mainsites':mainsites,}) 
def show_mainitems(request):  
    mainitems = Mainitems.objects.all()  
    return render(request,"mainitems.html",{'mainitems':mainitems, 'failed':False})  
def show_items(request):
    items = Items.objects.all()  
    return render(request,"items.html",{'items':items, 'failed':False}) 
def guides1(request):
    Modells = Guides.objects.all()  
    return render(request,"models.html",{'modells':Modells, 'failed':False}) 
def edit(request, id):  
    survey1 = Survey.objects.get(id=id)
    return render(request,'edit.html', {'Survey':survey1, 'failed':False})  
def update(request, id): 
    survey1 = Survey.objects.get(id=id)  
    form = SurveyForm(instance = survey1)
    if request.method == 'POST':
        form = SurveyForm(request.POST, instance = survey1)  
        if form.is_valid():  
            form.save()  
            return redirect("../show") 
    return render(request, 'edit.html', {'Survey': survey1 , 'failed':form.errors})  

def destroy(request, ID):  
    survey1 = Survey.objects.get(ID=ID)  
    survey1.delete()  
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