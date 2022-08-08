import csv
from http.client import HTTPResponse
import logging
from pyexpat.errors import messages
from urllib.request import HTTPRedirectHandler

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

# from rest_framework import serializers, viewsets
from pyexpat import model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
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
    return render(request, "Main.html")


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
    return render(request, 'index.html', {'form': form})


def show(request):
    surveys = Survey.objects.all()
    return render(request, "show.html", {'surveys': surveys})


def show_statuses(request):
    statuses = Statuses.objects.all()
    return render(request, "Statuses table.html", {'statuses': statuses, })


def show_manufacturers(request):
    manufacturers = Manufacturers.objects.all()
    return render(request, "manufacturer.html", {'manufacturers': manufacturers, })


def show_mainsites(request):
    mainsites = Mainsites.objects.all()
    return render(request, "mainsites.html", {'mainsites': mainsites, })


def show_mainitems(request):
    mainitems = Mainitems.objects.all()
    return render(request, "mainitems.html", {'mainitems': mainitems, 'failed': False})


def show_items(request):
    items = Items.objects.all()
    return render(request, "items.html", {'items': items, 'failed': False})


def guides1(request):
    Modells = Guides.objects.all()
    return render(request, "models.html", {'modells': Modells, 'failed': False})


def edit(request, id):
    survey1 = Survey.objects.get(id=id)
    return render(request, 'edit.html', {'Survey': survey1, 'failed': False})


def update(request, id):
    survey1 = Survey.objects.get(id=id)
    form = SurveyForm(instance=survey1)
    if request.method == 'POST':
        form = SurveyForm(request.POST, instance=survey1)
        if form.is_valid():
            form.save()
            return redirect("../show")
    return render(request, 'edit.html', {'Survey': survey1, 'failed': form.errors})


def destroy(request, ID):
    survey1 = Survey.objects.get(ID=ID)
    survey1.delete()
    return redirect("../show")


def add(request):
    form = SurveyForm
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to any page you wish to send the user after registration
            redirect('../show')
    context = {'form': form}
    return render(request, 'addSurvey.html', context)


def addFromCSV(request):
	if "GET" == request.method:
		return render(request, 'addSurveyFromCSV.html')
    # if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request, 'File is not CSV type')
			return render(request, 'addSurveyFromCSV.html')

        # if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request, "Uploaded file is too big (%.2f MB)." %
			               (csv_file.size/(1000*1000),))
			return render(request, 'addSurveyFromCSV.html')
		file_data = csv_file.read().decode("utf-8")

		lines = file_data.split("\n")
		# loop over the lines and save them in db. If error , store as string and then display
		for line in lines:
			fields = line.split(",")
			data_dict = {}
			data_dict["barcode"] = fields[0]
			data_dict["item"] = fields[1]
			data_dict["item_name"] = fields[2]
			data_dict["item_class"] = fields[3]
			data_dict["item_status"] = fields[4]
			data_dict["manufacturer_code"] = fields[5]
			data_dict["m_model_code"] = fields[6]
			data_dict["m_serial"] = fields[7]
			data_dict["piba_name"] = fields[8]
			data_dict["main_item_name"] = fields[9]
			data_dict["main_item_code"] = fields[10]
			data_dict["sub_site_name"] = fields[11]
			data_dict["location"] = fields[12]
			data_dict["checked_by"] = fields[13]
			data_dict["checked_date"] = fields[14]
			data_dict["remarks"] = fields[15]
			data_dict["actions"] = fields[16]
			try:
				form = SurveyForm(data_dict)
				if form.is_valid():
					form.save() 
                    # return redirect('../show')
                    # redirect('../show')
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())
			except Exception as e:
				logging.getLogger("error_logger").error(repr(e))
				pass

	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request, "Unable to upload file. "+repr(e))
    
	return HttpResponseRedirect(redirect_to='show')

    
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
