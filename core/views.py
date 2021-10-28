
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import activate, get_language_info
from django.utils import translation
import django.utils.translation
from project import settings
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.db.models import Count
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404


def home(request):
	headers = Header.objects.all()
	abouts = About.objects.all()
	Why_home = why_home.objects.all()
	Clients = Client.objects.all()
	Mision_visions = mision_vision.objects.all()
	services = Service.objects.all()
	projects_in = Projects_in.objects.all()
	subCategory = SubCategory.objects.all()
	tag = Tag.objects.all()


	
	# projects = Project.objects.annotate(
	# 	Count('project_name')).order_by('-project_name__count')[:5]
	context = {
			'Why_home': Why_home, 
			'Mision_visions': Mision_visions, 
			'headers': headers,
			'abouts': abouts,
			'Clients': Clients, 
		
			'services': services, 
			'projects_in': projects_in,
			'subCategory':subCategory,
			'tag':tag,
			}
	return render(request, 'core/index.html', context)
""" Project.objects.annotate(
		Count('project_name_en')).order_by('-project_name_en__count')[:5] """


def productHdl(request):
	headers = Header.objects.all()
	productHdl = ProductHdl.objects.annotate(Count('name')).order_by('-name__count')[:5]
	context={
		'headers':headers,
		'productHdl':productHdl
	}
	return render(request , 'core/producthdl.html',context)
def buspro(request):
	producthdl =ProductHdl.objects.filter(SubCategory='Buspro')
	headers = Header.objects.all()
	context={
		'headers':headers,
		'productHdl':productHdl
	}
	return render(request , 'core/buspro.html',context)

def knx(request):
	producthdl =ProductHdl.objects.filter(SubCategory='Knx')
	headers = Header.objects.all()
	context={
		'headers':headers,
		'productHdl':productHdl
	}
	return render(request , 'core/knx.html',context)
